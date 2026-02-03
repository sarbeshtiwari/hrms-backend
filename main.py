from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.employee import router as employee_router
from routers.attendance import router as attendance_router

app = FastAPI(title="HRMS API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(employee_router)
app.include_router(attendance_router)
