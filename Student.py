import datetime
from Datamanager import Datamanager
class Student:
    def __init__(self, first_name, last_name, email, date_of_birth, date_of_enroll=None, student_id=None):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth
        self.date_of_enroll = date_of_enroll

    def save_to_db(self, db_manager: Datamanager):
        cursor = db_manager.conn.cursor()
        date_of_enroll = datetime.datetime.now().strftime("%Y-%m-%d")
        cursor.execute(
            """INSERT INTO students (first_name, last_name, email, date_of_birth,date_of_enroll)
            VALUES (?, ?, ?, ?, ?)""",
            (self.first_name, self.last_name, self.email, self.date_of_birth, date_of_enroll),
        )
        db_manager.conn.commit()


    @staticmethod
    def get_all_students(db_manager: Datamanager):
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT id, first_name, last_name, email, date_of_birth, date_of_enroll FROM students")
        result = cursor.fetchall()
        students = []
        for row in result:
            students.append(
                Student(
                    student_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    date_of_birth=row[4],
                    date_of_enroll=row[5],
                )
            )
        return students

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} (Email: {self.email})"
    @staticmethod
    def update_grade(db_manager: Datamanager, grade,student_id,assignment_id):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """UPDATE grades
            SET grade = ?
            WHERE student_id = ? AND assignment_id = ?""",
            (grade,student_id,assignment_id),
        )
        db_manager.conn.commit()
    @staticmethod
    def delete_from_db(db_manager: Datamanager,student_id):
        cursor = db_manager.conn.cursor()
        
        cursor.execute(
            """DELETE FROM grades
            WHERE student_id = ?""",
            (student_id,),
        )
        
        cursor.execute(
            """DELETE FROM students
            WHERE id = ?""",
            (student_id,),
        )
        db_manager.conn.commit()
    @staticmethod
    def search_students_by_dob(db_manager: Datamanager, start_date: str, end_date: str):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """SELECT id, first_name, last_name, email, date_of_enroll
            FROM students
            WHERE date_of_enroll BETWEEN ? AND ?""",
            (start_date, end_date),
        )
        result = cursor.fetchall()
        students = []
        for row in result:
            students.append(
                Student(
                    student_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    date_of_enroll=row[4],
                )
            )
        return students
    