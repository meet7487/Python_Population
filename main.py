from fastapi import FastAPI

from model import Student, Course

from crud import (
    create_course,
    create_student,
    get_students
)

app = FastAPI()

@app.get("/")
async def home():

    return {
        "message": "Population API is working"
    }

# Create Course
@app.post("/courses")
async def add_course(course: Course):

    course_id = await create_course(course)

    return {
        "message": "Course created",
        "course_id": course_id
    }

# Create Student
@app.post("/students")
async def add_student(student: Student):

    student_id = await create_student(student)

    return {
        "message": "Student created",
        "student_id": student_id
    }

# Get Students with populated Course
@app.get("/students")
async def get_all_students():
    return await get_students()