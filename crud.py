from sqlalchemy.orm import Session
from models import Student, Course, Grade


# CREATE
def create_student(db: Session, first_name: str, last_name: str, faculty: str):
    student = Student(first_name=first_name, last_name=last_name, faculty=faculty)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


# READ
def get_students(db: Session):
    return db.query(Student).all()


# UPDATE
def update_student(db: Session, student_id: int, faculty: str):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        student.faculty = faculty
        db.commit()
    return student


# DELETE
def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student


# Фильтры

def get_students_by_faculty(db: Session, faculty: str):
    return db.query(Student).filter(Student.faculty == faculty).all()


def get_unique_courses(db: Session):
    return db.query(Course.name).distinct().all()


def get_low_grades(db: Session, course_name: str):
    return db.query(Student).join(Grade).join(Course).filter(
        Course.name == course_name,
        Grade.grade < 30
    ).all()


def get_avg_by_faculty(db: Session, faculty: str):
    from sqlalchemy import func
    return db.query(func.avg(Grade.grade)).join(Student).filter(
        Student.faculty == faculty
    ).scalar()


import csv

def load_from_csv(db: Session, file_path: str):
    with open(file_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            last_name, first_name, faculty, course_name, grade = row

            student = Student(first_name=first_name, last_name=last_name, faculty=faculty)
            course = Course(name=course_name)

            db.add(student)
            db.add(course)
            db.commit()

            grade_obj = Grade(
                student_id=student.id,
                course_id=course.id,
                grade=int(grade)
            )
            db.add(grade_obj)
            db.commit()
