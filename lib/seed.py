from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///students_courses.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for _ in range(15):
        course = Course.create(session, fake.sentence())
        for _ in range(random.randint(1, 5)):
            Student.create(session, fake.name(), course.id)

    session.close()

    
    