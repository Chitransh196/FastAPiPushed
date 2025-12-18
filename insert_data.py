from Student_project import Session
from models import Department, Student

from Student_project import Session
from models import Department, Student

session = Session()

department = Department(name="CSE")
session.add(department)
session.commit()

student1 = Student(name="Nattu", dept_id=department.id)
student2 = Student(name="Chitransh", dept_id=department.id)

# session.add(student1)
# session.add(student2)
session.commit()

session.close()
