from pydantic import BaseModel


class Course(BaseModel):
    name: str
    duration: str
    student_id:str


class Student(BaseModel):
    name: str
    email: str
