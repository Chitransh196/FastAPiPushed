from fastapi import FastAPI
from Student_project import Session
from models import Student, Department, DepartmentCreate, StudentsCreate

app = FastAPI()
session=Session()
@app.get("/Student")
def get_students():
    session
    students = session.query(Student).all()
    result = []

    for s in students:
        result.append({
            "id": s.id,
            "name": s.name,
            "dept_id": s.dept_id
        })

    session.close()
    return result

@app.get("/departments")
def get_departments():
    session = Session()

    departments = session.query(Department).all()
    result = []

    for d in departments:
        result.append({
            "id": d.id,
            "name": d.name
        })

    session.close()
    return result

@app.post("/departments")
def post_department(dept=DepartmentCreate):
    session 
    depart= Department(name=dept.name)
    session.add(depart)
    session.commit()
    session.close()
    return {"department added"}

@app.post("/students")
def post_Student(std=StudentsCreate):
    std1=Student(name=std.name,
                 dept_id=std.dept_id)
    session.add(std1)
    session.commit()
    session.close()