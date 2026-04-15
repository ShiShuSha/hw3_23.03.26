from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@app.post("/students")
def create_student(first_name: str, last_name: str, faculty: str, db: Session = Depends(get_db)):
    return crud.create_student(db, first_name, last_name, faculty)


# READ
@app.get("/students")
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, faculty: str, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, faculty)


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_id)


# ФИЛЬТРЫ

@app.get("/students/faculty/{faculty}")
def students_by_faculty(faculty: str, db: Session = Depends(get_db)):
    return crud.get_students_by_faculty(db, faculty)


@app.get("/courses")
def unique_courses(db: Session = Depends(get_db)):
    return crud.get_unique_courses(db)


@app.get("/students/low-grades/{course}")
def low_grades(course: str, db: Session = Depends(get_db)):
    return crud.get_low_grades(db, course)


@app.get("/avg/{faculty}")
def avg_grade(faculty: str, db: Session = Depends(get_db)):
    return crud.get_avg_by_faculty(db, faculty)




from fastapi import Header, HTTPException
from auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)


def get_current_user(user_id: int = Header(None)):
    if user_id is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user_id
