from Datamanager import Datamanager
from Student import Student
class Assignment:
    def __init__(self, name, description, lecturer_id, assignment_id=None):
        self.id = assignment_id
        self.name = name
        self.description = description
        self.lecturer_id = lecturer_id

    def save_to_db4(self, db_manager: Datamanager):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """INSERT INTO assignments (name, description, lecturer_id)
            VALUES (?, ?, ?)""",
            (self.name, self.description, self.lecturer_id),
        )
        db_manager.conn.commit()

    @staticmethod
    def get_all_assignments(db_manager: Datamanager):
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT id, name, description, lecturer_id FROM assignments")
        result = cursor.fetchall()
        assignments = []
        for row in result:
            assignments.append(
                Assignment(
                    assignment_id=row[0],
                    name=row[1],
                    description=row[2],
                    lecturer_id=row[3],
                )
            )
        return assignments

    def __str__(self):
        return f"Assignment: {self.name}, description: {self.description}, Lecturer ID: {self.lecturer_id}"
    @staticmethod
    def get_assignments_by_lecturer( db_manager: Datamanager, lecturer_id: int):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """SELECT id, name, description, lecturer_id 
                FROM assignments 
                WHERE lecturer_id = ?""",
            (lecturer_id,),
        )
        result = cursor.fetchall()
        assignments = []
        for row in result:
            assignments.append(
                Assignment(
                    assignment_id=row[0],
                    name=row[1],
                    description=row[2],
                    lecturer_id=row[3],
            )
        )
        return assignments
    @staticmethod
    def add_assignment(db_manager: Datamanager, assignment_name: str,lecturer_id: int):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """INSERT INTO assignments (name, lecturer_id) VALUES (?, ?)""",
            (assignment_name, lecturer_id),
        )
        assignment_id = cursor.lastrowid
        db_manager.conn.commit()

        # Add default grades for all students
        students = Student.get_all_students(db_manager)
        for student in students:
            cursor.execute(
                """INSERT INTO grades (student_id, assignment_id, grade) VALUES (?, ?, 0)""",
                (student.id, assignment_id),
            )
        db_manager.conn.commit()