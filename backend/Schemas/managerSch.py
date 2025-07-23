from pydantic import BaseModel, EmailStr

class ManagerBase(BaseModel):
    username: str
    email: EmailStr  # Validates proper email format

class ManagerCreate(ManagerBase):
    password: str  # Plain text password sent by client

class ManagerOut(ManagerBase):
    id: int

    class Config:
        orm_mode = True
        
class ManagerUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    
    class Config:
        orm_mode = True
        
class ManagerLogin(BaseModel):
    email: EmailStr 
    password: str
    