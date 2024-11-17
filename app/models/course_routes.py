from fastapi import APIRouter, HTTPException
from app.models.course_model import Course
from typing import List
from pydantic import BaseModel

router = APIRouter()

class CourseCreate(BaseModel):
    title: str
    description: str

# Создание курса
@router.post("/courses/", response_model=Course)
async def create_course(course: CourseCreate):
    new_course = Course(title=course.title, description=course.description)
    # Здесь нужно добавить логику сохранения в базу данных
    return new_course

# Получение всех курсов
@router.get("/courses/", response_model=List[Course])
async def get_courses():
    # Здесь нужно добавить логику получения курсов из базы данных
    return [{"title": "Python Basics", "description": "Learn Python from scratch"}]
