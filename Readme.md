HRMS Backend API

The HRMS Backend API is built using FastAPI and MongoDB to manage employees, attendance, and other HR-related operations. The backend is fully asynchronous and provides a REST API suitable for integration with modern frontend frameworks like React or Vue.

Features

CRUD operations for employees
Mark and track employee attendance
Upsert attendance per employee and date
Fully asynchronous operations with Motor (MongoDB)
CORS enabled for frontend integration
Interactive API documentation via Swagger and ReDoc

Project Structure

backend/
├─ main.py               # FastAPI application entrypoint
├─ database.py           # MongoDB connection and serialization helpers
├─ models/               # Pydantic models for request/response validation
│  ├─ employee.py
│  └─ attendance.py
├─ routers/              # API routers
│  ├─ employees.py
│  └─ attendance.py

Setup Instructions
1. Clone the repository
git clone 
cd backend

2. Create a virtual environment
Linux / macOS
python3 -m venv venv
source venv/bin/activate

Windows
python -m venv venv
venv\Scripts\activate

3. Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

4. Configure MongoDB

Ensure MongoDB is running. By default, the connection URL is:

mongodb+srv://rahul8454454singh_db_user:RTy3kh8TTiwunUQe@cluster0.ln3yg2l.mongodb.net/?appName=hrms


The default database used is hrms.

You can update the URL in database.py if needed.

5. Run the application
uvicorn main:app --reload


Base URL: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

ReDoc UI: http://127.0.0.1:8000/redoc

API Endpoints

Employees

GET	/api/employees	Get all employees
GET	/api/employees/{id}	Get a single employee
POST	/api/employees	Create a new employee
DELETE	/api/employees/{id}	Delete an employee

Attendance
GET	/api/attendance	Get all attendance records
POST	/api/attendance	Mark or update attendance for an employee
Pydantic Models
Employee Models

EmployeeCreate (Request)

{
  "employeeId": "EMP001",
  "fullName": "John Doe",
  "email": "john@example.com",
  "department": "Engineering"
}


Employee Response

{
  "id": "64d3b8f1e4a3c9f123456789",
  "employeeId": "EMP001",
  "fullName": "John Doe",
  "email": "john@example.com",
  "department": "Engineering",
  "createdAt": "2026-02-03T12:34:56.789Z"
}

Attendance Models

AttendanceCreate (Request)

{
  "employeeId": "EMP001",
  "date": "2026-02-03",
  "status": "present"
}


Attendance Response

{
  "id": "64d3b8f1e4a3c9f123456790",
  "employeeId": "EMP001",
  "date": "2026-02-03",
  "status": "present",
  "createdAt": "2026-02-03T12:45:12.123Z"
}

Notes

Attendance POST endpoint performs an upsert, i.e., if a record exists for the employee and date, it updates the status. Otherwise, it creates a new record.

All endpoints return data with serialized _id fields as id (string).

CORS is enabled for all origins, methods, and headers to simplify frontend integration.