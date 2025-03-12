import sys
from lib.db import Session
from lib.models import Student, Course, Enrollment

def main_menu():
    while True:
        print("\nStudent Course Registration System")
        print("1. Manage Students")
        print("2. Manage Courses")
        print("3. Enroll Student in Course")
        # print("4. View Student Course Enrollment")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            enroll_student_in_course()
        # elif choice == "4":
        #     view_student_course_enrollment()
        elif choice == "4":
            print("Exiting...Goodbye!")
        else:
            print("Invalid choice. Please try again.")

def student_menu(): 
    session = Session()
    while True:
        print("\nManage Students")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. View All Students")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            student = Student(name=name, email=email)
            session.add(student)
            session.commit()
            print("Student added successfully!")

        elif choice == "2":
            name = input("Enter student ID to delete: ")
            student = session.query(Student).filter_by(id=student_id).first()
            if student:
                session.delete(student)
                session.commit()
                print("Student deleted successfully!")
            else:
                print("Student not found!")

        elif choice == "3":
            name = input("Enter student ID to update: ")
            student = session.query(Student).filter_by(id=student_id).first()
            if student:
                name = input("Enter new student name: ")
                email = input("Enter new student email: ")
                student.name = name
                student.email = email
                session.commit()
                print("Student updated successfully!")
            else:
                print("Student not found!")

        elif choice == "4":
            students = session.query(Student).all()
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Email: {student_email}")


        elif choice == "5":
            break

        else:
            print("Invalid choice. Please choose a valid option.")

    session.close()

    def course_menu():
        session = Session()
        while True:
            print("\nCourse Menu:")
            print("1. Add Course")
            print("2. View Courses")
            print("3. Delete Course")
            print("4. Update Course")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter course name: ")
                description = input("Enter course description: ")
                course = Course(name=name, description=description)
                session.add(course)
                session.commit()
                print("Course added successfully!")
            
            elif choice == "2":
                courses = session.query(Course).all()
                for course in courses:
                    print(course)

            elif choice == "3":
                course_id = input("Enter course ID to delete: ")
                course = session.query(Course).filter(Course.id == course_id).first()
                if course:
                    session.delete(course)
                    session.commit()
                    print("Course deleted successfully!")
                else:
                    print("Course not found!")

            elif choice == "4":
                course_id = input("Enter course ID to update: ")
                course = session.query(Course).filter(Course.id == course_id).first()
                if course:
                    course.name = input("Enter new course name: ")
                    course.description = input("Enter new course description: ")
                    session.commit()
                    print("Course updated successfully!")
                else:
                    print("Course not found!")

            elif choice == "5":
                break

            else:
                print("Invalid choice. Please try again.")
        session.close()

    def enroll_student():
        session = Session()
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        student = session.query(Student).filter_by(id=student_id).first()
        course = session.query(Course).filter_by(id=course_id).first()
    
        if student and course:
            enrollment = Enrollment(student_id=student_id, course_id=course_id)
            session.add(enrollment)
            session.commit()
            print("Student enrolled successfully!")
        else:
            print("Invalid student or course ID.")
        session.close()

if __name__ == "__main__":
    main_menu()