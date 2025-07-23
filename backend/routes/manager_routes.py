from fastapi import APIRouter, Depends, HTTPException, Request

from sqlalchemy.orm import Session
from backend.crud import managerCrud
from backend.Schemas import managerSch
from ..database import get_db
from .. import auth
from ..auth import token_checker


router = APIRouter()



@router.get('/getManager/{manager_id}')
def getManager(manager_id: int, request: Request, db: Session = Depends(get_db), token: str = Depends(token_checker)):
    return auth.token_checker(request, db)




@router.post('/createManager')
def createManager(manager: managerSch.ManagerCreate, db: Session = Depends(get_db)):
    manager_db = managerCrud.createManager(db, manager)
    

@router.patch('/updateManager')
def updateManager(id_manager: int, manager: managerSch.ManagerUpdate, db: Session = Depends(get_db)):
    
    updated_manager = managerCrud.updateManager(db, manager, id_manager)
    return updated_manager


@router.delete('/deleteManager/{email}')
def deleteManager(email: str, db: Session = Depends(get_db)):
    manager = managerCrud.deleteManager(db, email)
    if not manager:
        return 'Sorry, this manager is not exist in our database'
    
    return f'The manager with email {manager.email} has been deleted successfully'


@router.post('/loginManager')
def loginManager(request: Request, email: str, password: str, db: Session = Depends(get_db)):
    return auth.authentification(request, db, email, password)