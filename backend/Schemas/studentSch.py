from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    username: str
    email: EmailStr
    
class StudentCreate(StudentBase):
    password: str
    
class StudentOut(StudentBase):
    id: int
    
    class Config:
        orm_mode = True
        

class StudentUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    
    class Config:
        orm_mode = True