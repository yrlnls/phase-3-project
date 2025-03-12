from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Course(Base):
       __tablename__ = 'courses'

       id = Column(Integer, primary_key=True)
       title = Column(String, nullable=False)
       students = relationship('Student', back_populates='course', cascade="all, delete")

       def __init__(self, title):
           self.title = title

       @classmethod
       def create(cls, session, title):
           course = cls(title=title)
           session.add(course)
           session.commit()
           return course

       @classmethod
       def delete(cls, session, course_id):
           course = cls.find(session, course_id)
           if course:
               session.delete(course)
               session.commit()

       @classmethod
       def get_all(cls, session):
           return session.query(cls).all()

       @classmethod
       def find(cls, session, course_id):
           return session.query(cls).filter_by(id=course_id).first()

class Student(Base):
       __tablename__ = 'students'

       id = Column(Integer, primary_key=True)
       name = Column(String, nullable=False)
       course_id = Column(Integer, ForeignKey('courses.id'))

       course = relationship('Course', back_populates='students')

       def __init__(self, name, course_id):
           self.name = name
           self.course_id = course_id

       @classmethod
       def create(cls, session, name, course_id):
           student = cls(name=name, course_id=course_id)
           session.add(student)
           session.commit()
           return student

       @classmethod
       def delete(cls, session, student_id):
           student = cls.find(session, student_id)
           if student:
               session.delete(student)
               session.commit()

       @classmethod
       def get_all(cls, session):
           return session.query(cls).all()

       @classmethod
       def find(cls, session, student_id):
           return session.query(cls).filter_by(id=student_id).first()