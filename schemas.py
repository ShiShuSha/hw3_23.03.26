from pydantic import BaseModel


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    faculty: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True


class CourseCreate(BaseModel):
    name: str


class GradeCreate(BaseModel):
    student_id: int
    course_id: int
    grade: int
