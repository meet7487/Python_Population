from bson import ObjectId

from db import student_collection, course_collection


# Create Course
async def create_course(course):

    result = await course_collection.insert_one(
        course.model_dump()
    )
    return str(result.inserted_id)


# Create Student
async def create_student(student):
    result = await student_collection.insert_one(
        student.model_dump()
    )
    return str(result.inserted_id)


# Get Students with Course
async def get_students():
    students = []
    async for student in student_collection.find():
        student_data = {
            "id": str(student["_id"]),
            "name": student["name"],
            "email": student["email"],
            "courses": []
        }
        # Fetch courses for the student
        async for course in course_collection.find({"student_id": str(student["_id"])}):
            course_data = {
                "id": str(course["_id"]),
                "name": course["name"],
                "duration": course["duration"]
            }
            student_data["courses"].append(course_data)
        students.append(student_data)
    return students