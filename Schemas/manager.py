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