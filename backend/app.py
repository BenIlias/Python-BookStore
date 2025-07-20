from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.crud import managerCrud, studentCrud
from .database import get_db, engine
from .Schemas import managerSch, studentSch
from . import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/createManager')
def createManager(manager: managerSch.ManagerCreate, db: Session = Depends(get_db)):
    manager_db = managerCrud.createManager(db, manager)
    

@app.get('/getManager/{manager_id}')
def getManager(manager_id: int, db: Session = Depends(get_db)):
    return managerCrud.get_manager_by_id(db, manager_id)


@app.delete('/deleteManager/{email}')
def deleteManager(email: str, db: Session = Depends(get_db)):
    manager = managerCrud.deleteManager(db, email)
    if not manager:
        return 'Sorry, this manager is not exist in our database'
    
    return f'The manager with email {manager.email} has been deleted successfully'


@app.patch('/updateManager')
def updateManager(id_manager: int, manager: managerSch.ManagerUpdate, db: Session = Depends(get_db)):
    
    updated_manager = managerCrud.updateManager(db, manager, id_manager)
    return updated_manager