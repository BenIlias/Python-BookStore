from sqlalchemy.orm import Session
from fastapi import Depends, Body
from backend.Schemas import managerSch, studentSch
from .. import models, auth


def get_manager_by_id(db: Session, manager_id: int):
    return db.query(models.Manager).filter(models.Manager.id == manager_id).first()    

def get_manager_by_email(db: Session, email: str):
    return db.query(models.Manager).filter(models.Manager.email == email).first()
    
def createManager(db: Session, manager:  managerSch.ManagerCreate):
    if get_manager_by_email(db, manager.email):
        return None
    
    manager_dict = manager.dict()
    manager_dict['hashed_password'] = auth.get_hashed(manager_dict.pop('password'))
    manager_db = models.Manager(**manager_dict)
    db.add(manager_db)
    db.commit()
    db.refresh(manager_db)
    
    return manager_db
    
def updateManager(db: Session, manager: managerSch.ManagerUpdate, manager_id: int):
    manager_db = get_manager_by_id(db, manager_id)
    if not manager_db:
        return None
    manager_dict = manager.dict(exclude_unset=True)
    for key, value in manager_dict.items():
        setattr(manager_db, key, value)
    
    db.commit()
    db.refresh(manager_db)
    return manager_db






    
def deleteManager(db: Session, email: str):
    manager_db = get_manager_by_email(db, email)
    if manager_db is None:
        return None 
    db.delete(manager_db)
    db.commit()
    
    
    return manager_db
    

    
    
    