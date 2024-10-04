from Datamanager import Datamanager
from Lecturer import Lecturer
from Grades import Grade
from assignments import Assignment
from datetime import date
from Student import Student

def main():
    db_manager = Datamanager()
    print(Assignment.get_all_assignments(db_manager=db_manager))
    student = Student("alam", "Al kais", "example4@example.com", 2003)  # Create a Student object
    student.save_to_db(db_manager)
    lecturer=Lecturer("ehsan","lol","eda3ae@aa.com","2021-02-04","informatics engineering")
    lecturer.save_to_db_lec(db_manager)
    assignment = Assignment("programing", "Calculus Homework", 4)
    assignment.save_to_db4(db_manager)
    grade = Grade(90, 1, 2)
    grade.save_to_db_gr(db_manager)
    grade2 = Grade(93, 4, 2)
    grade2.save_to_db_gr(db_manager)
    all_assignments = Assignment.get_all_assignments(db_manager)
    for assignment in all_assignments:
        print(assignment)
    lecturer_id = 1  # replace with the actual lecturer ID
    assignments = Assignment.get_assignments_by_lecturer(db_manager, lecturer_id)
    for assignment in assignments:
        print(assignment)
    assignment_name = "New Assignment"
    lecturer_id = 1  # replace with the actual lecturer ID
    Assignment.add_assignment(db_manager, assignment_name, lecturer_id)
    all_grades = Grade.get_all_grades(db_manager)
    for grade in all_grades:
        print(grade)
    assignment_id = 1  # replace with the actual assignment ID

    grades = Grade.get_grades_by_assignment(db_manager, assignment_id)

    for grade in grades:
        print(grade)
    new_grade_value = 97  # replace with the new grade value
    Grade.update_grade(db_manager, new_grade_value,4,5)
    lecturers = Lecturer.get_all_lecturers(db_manager)

    for lecturer in lecturers:
        print(lecturer)
    search_query = "kh"  # replace with the search query
    lecturers = Lecturer.search_lecturers(db_manager, search_query)
    for lecturer in lecturers:
        print(lecturer)
    all_students = Student.get_all_students(db_manager)
    for student in all_students:
        print(f"Name: {student.first_name} {student.last_name}, DOB: {student.date_of_birth}")
    Student.update_grade(db_manager,77.5,1,5)
    Student.delete_from_db(db_manager,7)
    start_date = "2000-01-01"
    end_date = "2004-12-31"

    # Search for students by date of birth
    students = Student.search_students_by_dob(db_manager, "2000-01-01", "2004-12-31")

    for student in students:
        print(student)
    
    
    print("Done")
    
    print("hh\n")
    result=Student.search_students_by_dob(db_manager,"1995", "2005" )
    print(result)
    for student in result:
        print(f"Name: {student.first_name} {student.last_name}, DOB: {student.date_of_birth}")
    print("jjjj")
    
    db_manager.close()
if __name__ == "__main__":
    main()