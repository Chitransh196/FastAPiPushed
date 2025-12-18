from sqlalchemy import Column, Integer, String, ForeignKey
from Student_project import Base, engine
from pydantic import BaseModel
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", back_populates="department" )

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dept_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="students")

class DepartmentCreate(BaseModel):
    name: str

class StudentsCreate(BaseModel):
    name: str
    dept_id: str
    

Base.metadata.create_all(engine)