from .database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship



class Manager(Base):
    __tablename__ = 'managers'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    email = Column(String, nullable=False, index=True, unique=True)
    hashed_password = Column(String, nullable=False)


class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    email = Column(String, nullable=False, index=True, unique=True)
    hashed_password = Column(String, nullable=False)
    
    books = relationship('Book', back_populates='student')
    
    
    

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'))
    
    student = relationship('Student', back_populates='books')
    
    

