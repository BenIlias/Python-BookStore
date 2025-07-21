from sqlalchemy.orm import Session
from .. import models, auth
from backend.Schemas import studentSch, managerSch


def getStudentByID(db: Session, student_id):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def getStudentByEmail(db: Session, email):
    return db.query(models.Student).filter(models.Student.email == email).first()


def createStudent(db: Session, student: studentSch.StudentCreate):
    if getStudentByEmail(db, student.email):
        return None
    
    student_dict = student.dict()
    student_dict['hashed_password'] = auth.get_hashed(student_dict.pop('password'))
    
    student_db = models.Student(**student_dict)
    
    db.add(student_db)
    db.commit()
    db.refresh(student_db)
    
    return student_db

def deleteStudent(db: Session, student_id: int):
    student_db = getStudentByID(db, student_id)
    if not student_db:
        return None
    
    db.delete(student_db)
    db.commit()
    
    return student_db

def updateStudent(db: Session, student: studentSch.StudentUpdate, student_id: int):
    
    student_dict = student.dict(exclude_unset=True)
    if not student_dict:
        return None
    
    student_db = getStudentByID(db, student_id)
    if not student_db:
        return None
    
    if 'password' in student_dict:
        student_dict['hashed_password'] = auth.get_hashed(student_dict.pop('password'))
   
    for key, value in student_dict.items():
        setattr(student_db, key, value)
    
    db.commit()
    db.refresh(student_db)
    
    return student_db
    


    

