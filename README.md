# 🏋️‍♂️ Fitness Studio Booking API

A simple Django REST API for a fictional fitness studio, allowing clients to view upcoming classes, book a spot, and view their bookings.  
Supports timezone-aware class schedules, input validation, and logging.

---

## 🚀 Features

- **View Classes:** `GET /api/classes?tz=Asia/Kolkata`
- **Book a Class:** `POST /api/book_class`
- **View Bookings:** `GET /api/bookings?email=your@email.com`
- Timezone management for class times
- Input validation and error handling
- Logging of API activity
- Seed script for sample data

---

## 🛠️ Tech Stack

- Python 3, Django, Django REST Framework
- SQLite (in-memory, no setup required)

---

## ⚡ Setup Instructions

1. **Clone the repository**
   ```sh
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```sh
   python manage.py migrate
   ```

5. **Seed sample data**
   ```sh
   python manage.py seed_classes
   ```

6. **Start the development server**
   ```sh
   python manage.py runserver
   ```

---

## 🧪 Sample API Requests

### View Classes
```sh
curl "http://localhost:8000/api/classes?tz=Asia/Kolkata"
```

### Book a Class
```sh
curl -X POST "http://localhost:8000/api/book_class" ^
     -H "Content-Type: application/json" ^
     -d "{\"class_id\": 1, \"client_name\": \"John Doe\", \"client_email\": \"john@example.com\"}"
```

### View Bookings
```sh
curl "http://localhost:8000/api/bookings?email=john@example.com"
```

---

## 📦 Seed Data

Seed data for classes is provided via the custom management command:
```sh
python manage.py seed_classes
```
