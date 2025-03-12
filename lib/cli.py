import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course

engine = create_engine('sqlite:///students_courses.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def display_courses():
    courses = Course.get_all(session)
    if not courses:
        print("No courses available.")
    for course in courses:
        print(f"ID: {course.id}, Title: {course.title}")

def display_students():
    students = Student.get_all(session)
    if not students:
        print("No students available.")
    for student in students:
        course_title = (session.query(Course).filter_by(id=student.course_id).first().title 
                        if student.course_id else "No Course")
        print(f"ID: {student.id}, Name: {student.name}, Course: {course_title}")

def add_student():
    name = input("Enter student name: ")
    course_id = input("Enter course ID (or leave blank for no course): ")
    course_id = int(course_id) if course_id else None
    try:
        Student.create(session, name, course_id)
        print("Student added successfully.")
    except Exception as e:
        print(f"Error adding student: {e}")

def add_course():
    title = input("Enter course title: ")
    try:
        Course.create(session, title)
        print("Course added successfully.")
    except Exception as e:
        print(f"Error adding course: {e}")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    try:
        Student.delete(session, int(student_id))
        print("Student deleted successfully.")
    except Exception as e:
        print(f"Error deleting student: {e}")

def delete_course():
    course_id = input("Enter course ID to delete: ")
    try:
        Course.delete(session, int(course_id))
        print("Course deleted successfully.")
    except Exception as e:
        print(f"Error deleting course: {e}")

def find_student():
    student_id = input("Enter student ID to find: ")
    student = Student.find(session, int(student_id))
    if student:
        print(f"Found Student - ID: {student.id}, Name: {student.name}, Course ID: {student.course_id}")
    else:
        print("Student not found.")

def find_course():
    course_id = input("Enter course ID to find: ")
    course = Course.find(session, int(course_id))
    if course:
        print(f"Found Course - ID: {course.id}, Title: {course.title}")
    else:
        print("Course not found.")

def update_student():
    student_id = input("Enter student ID to update: ")
    student = Student.find(session, int(student_id))
    if student:
        new_name = input("Enter new name: ")
        new_course_id = input("Enter new course ID (or leave blank for no course): ")
        new_course_id = int(new_course_id) if new_course_id else None
        student.name = new_name
        student.course_id = new_course_id
        session.commit()
        print("Student updated successfully.")
    else:
        print("Student not found.")


def update_course():
    course_id = input("Enter course ID to update: ")
    course = Course.find(session, int(course_id))
    if course:
        new_title = input("Enter new title: ")
        course.title = new_title
        session.commit()
        print("Course updated successfully.")
    else:
        print("Course not found.")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Students")
        print("2. Manage Courses")
        print("3. Exit")

        choice = input("Select an option: ")
        if choice == '1':
            students_menu()
        elif choice == '2':
            courses_menu()
        elif choice == '3':
            print("Exiting the application...")
            session.close()
            sys.exit()
        else:
            print("Invalid choice, please try again.")

def students_menu():
    while True:
        print("\nStudents Menu")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Display All Students")
        print("4. Find Student by ID")
        print("5. Update Student")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            display_students()
        elif choice == '4':
            find_student()
        elif choice == '5':
            update_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def courses_menu():
    while True:
        print("\nCourses Menu")
        print("1. Add Course")
        print("2. Delete Course")
        print("3. Display All Courses")
        print("4. Find Course by ID")
        print("5. Update Course")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == '1':
            add_course()
        elif choice == '2':
            delete_course()
        elif choice == '3':
            display_courses()
        elif choice == '4':
            find_course()
        elif choice == '5':
            update_course()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
