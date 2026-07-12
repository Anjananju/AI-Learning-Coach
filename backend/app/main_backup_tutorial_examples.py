from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
students = []

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Learning Coach 🚀"
    }

@app.get("/about")
def about():
    return {
        "app": "AI Learning Companion",
        "version": "1.0",
        "author": "Anjana"
    }

@app.get("/course/{course_id}")
def get_course(course_id: int):
    return {
        "course_id": course_id
    }

#optional querynparameter
@app.get("/search")
def search(topic: str="AI"):
    return {
        "topic": topic
    }

#multiple query parameters
@app.get("/courses")
def courses(level: str, duration: int):
    return {
        "level": level,
        "duration": duration
    }
#optional multiple query parameters
@app.get("/learn")
def learn(topic: str = "Python", difficulty: str = "Beginner"):
    return {
        "topic": topic,
        "difficulty": difficulty,
        "message": f"Learning {topic} at {difficulty} level."
    }

class Student(BaseModel):
    name: str
    email: str
    experience: int

@app.post("/student")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student registered successfully!",
        "student": student
    }

@app.get("/students")
def get_students():
    return students


#get specific student details
@app.get("/student/{student_id}")
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        return {
            "message": "Student not found"
        }

    return students[student_id]

@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id < 0 or student_id >= len(students):
        return {
            "message": "Student not found"
        }

    students[student_id] = student

    return {
        "message": "Student updated successfully",
        "student": student
    }


@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        return {
            "message": "Student not found"
        }

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }
