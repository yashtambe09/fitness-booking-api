from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.utils.timezone import make_aware
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer, BookingCreateSerializer
from pytz import timezone as pytz_timezone
import logging

logger = logging.getLogger('booking_api')

@api_view(['GET'])
def get_classes(request):
    tz = request.GET.get('tz', 'Asia/Kolkata')
    logger.info(f"GET /api/classes called with tz={tz} by {request.user if hasattr(request, 'user') and request.user.is_authenticated else 'User'}")
    classes = FitnessClass.objects.filter(datetime__gte=timezone.now()).order_by('datetime')
    # Convert class times to requested timezone
    for c in classes:
        c.datetime = c.datetime.astimezone(pytz_timezone(tz))
    serializer = FitnessClassSerializer(classes, many=True)
    logger.debug(f"Classes returned: {serializer.data}")
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    logger.info(f"POST /api/book_class called with data={request.data} by {request.user if hasattr(request, 'user') and request.user.is_authenticated else 'User'}")
    serializer = BookingCreateSerializer(data=request.data)
    if not serializer.is_valid():
        logger.warning(f"Booking creation failed due to invalid data: {serializer.errors}")
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    data = serializer.validated_data
    try:
        fitness_class = FitnessClass.objects.get(id=data['class_id'])
    except FitnessClass.DoesNotExist:
        logger.warning(f"Booking creation failed: Class with id {data['class_id']} not found.")
        return Response({'error': 'Class not found.'}, status=status.HTTP_404_NOT_FOUND)
    if fitness_class.available_slots < 1:
        logger.warning(f"Booking creation failed: No slots available for class id {data['class_id']}.")
        return Response({'error': 'No slots available.'}, status=status.HTTP_400_BAD_REQUEST)
    booking = Booking.objects.create(
        fitness_class=fitness_class,
        client_name=data['client_name'],
        client_email=data['client_email']
    )
    fitness_class.available_slots -= 1
    fitness_class.save()
    logger.info(f"Booking created: {booking}")
    return Response({'message': 'Booking successful.'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_bookings(request):
    email = request.GET.get('email')
    logger.info(f"GET /api/bookings called with email={email} by {request.user if hasattr(request, 'user') and request.user.is_authenticated else 'User'}")
    if not email:
        logger.warning("Bookings fetch failed: Email is required but not provided.")
        return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    logger.debug(f"Bookings returned for {email}: {serializer.data}")
    return Response(serializer.data)
