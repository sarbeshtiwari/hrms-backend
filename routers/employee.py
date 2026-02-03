from fastapi import APIRouter, HTTPException
from models.employee import Employee, EmployeeCreate
from database import db, serialize_doc
from datetime import datetime
from bson import ObjectId

router = APIRouter(prefix="/api/employees", tags=["Employees"])
employees_collection = db.employees

# GET all employees
@router.get("/", response_model=list[Employee])
async def get_employees():
    employees = []
    async for e in employees_collection.find():
        employees.append(serialize_doc(e))
    return employees

# GET employee by ID
@router.get("/{employee_id}", response_model=Employee)
async def get_employee(employee_id: str):
    employee = await employees_collection.find_one({"_id": ObjectId(employee_id)})
    if employee:
        return serialize_doc(employee)
    raise HTTPException(status_code=404, detail="Employee not found")

# POST create employee
@router.post("/", response_model=Employee)
async def create_employee(employee: EmployeeCreate):
    data = employee.dict()
    data["createdAt"] = datetime.utcnow()
    result = await employees_collection.insert_one(data)
    new_employee = await employees_collection.find_one({"_id": result.inserted_id})
    return serialize_doc(new_employee)


# DELETE employee
@router.delete("/{id}")
async def delete_employee(id: str):
    result = await employees_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"success": True}
