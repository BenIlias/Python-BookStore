from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.crud import studentCrud
from backend.Schemas import studentSch
from ..database import get_db



router = APIRouter()

@router.get('/getStudent')
def getStudent(student_id: int, db: Session = Depends(get_db)):
    return studentCrud.getStudentByID(db, student_id)


@router.post('/createStudent')
def createStudent(student: studentSch.StudentCreate, db: Session = Depends(get_db)):
    
    if studentCrud.getStudentByEmail(db, student.email):
        return None
    return studentCrud.createStudent(db, student)



@router.patch('/updateStudent')
def updateStudent(student: studentSch.StudentUpdate, student_id, db: Session = Depends(get_db)):
    return studentCrud.updateStudent(db, student, student_id)




@router.delete('/deleteStudent')
def deleteStudent(student_id: int, db: Session = Depends(get_db)):
    student_db = studentCrud.deleteStudent(db, student_id)
    if not student_db:
        raise HTTPException(400, detail='Sorry, this user does not exist')
    
    return f'The user {student_db.username} has been deleted successfully'