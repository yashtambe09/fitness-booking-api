from django.core.management.base import BaseCommand
from booking_api.models import FitnessClass
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample fitness classes.'

    def handle(self, *args, **kwargs):
        FitnessClass.objects.all().delete()
        now = timezone.now()
        classes = [
            FitnessClass(
                name='Yoga',
                datetime=now + timedelta(days=1, hours=7),
                instructor='Alice',
                total_slots=10,
                available_slots=10
            ),
            FitnessClass(
                name='Zumba',
                datetime=now + timedelta(days=2, hours=18),
                instructor='Bob',
                total_slots=15,
                available_slots=15
            ),
            FitnessClass(
                name='HIIT',
                datetime=now + timedelta(days=3, hours=6),
                instructor='Charlie',
                total_slots=12,
                available_slots=12
            ),
        ]
        FitnessClass.objects.bulk_create(classes)
        self.stdout.write(self.style.SUCCESS('Sample fitness classes seeded.'))
