from fastapi import FastAPI
from Student_project import Session
from models import Student, Department

app = FastAPI()

@app.get("/Student")
def get_students():
    session = Session()

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

