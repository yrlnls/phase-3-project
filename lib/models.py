from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    age = Column(Integer(), nullable=False)
    email = Column(String(), nullable=False)

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, email={self.email})"
    
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    