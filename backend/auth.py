from fastapi import Request, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import models
from datetime import timedelta, datetime
from jose import jwt, JWTError
from backend.crud import managerCrud
from .database import get_db


MYJWT_KEY = 'encdectoken'
pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')



def get_hashed(password: str):
    return pwd_context.hash(password)

def verify_hash(password, hashed_password):
    return pwd_context.verify(password, hashed_password)
    
    


def token_generator(data: dict, expiry_date: timedelta = None):
    to_code = data.copy()
    if expiry_date:
        to_code.update({'exp': datetime.utcnow()} + expiry_date)
    else:
        to_code.update({'exp': datetime.utcnow() + timedelta(minutes=15)})
    
    access_token = jwt.encode(to_code, MYJWT_KEY)
    return access_token


def decode_token(token: str, db: Session):
    try:
        payload = jwt.decode(token, MYJWT_KEY)
        username = payload.get('username')
        if username is None:
            return None
        
        username_db = managerCrud.get_manager_by_username(db, username)
        print(username)
        if username_db:
            return username
        
        
    except JWTError:
        raise HTTPException(404, detail='The token is invalid')


def token_checker(request: Request, db: Session):
    try:
        token = request.headers.get('Authorization').split(' ')[1]
        username = decode_token(token, db)
        if not username:
            return None
        return username
    
    except:
        return 'The token is invalid'

def authentification(request: Request, db: Session, email: str, password: str):
    manager_db = managerCrud.get_manager_by_email(db, email)
    if not manager_db:
        return None
    
    if not verify_hash(password, manager_db.hashed_password):
        return None
    
    access_token = token_generator({'username': manager_db.username})
    
    return {'Token': access_token}
    
    
    
    
    


