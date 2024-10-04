import sqlite3

class Datamanager:
    def __init__(self, db_name="university.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                date_of_birth TEXT,
                date_of_enroll TEXT DEFAULT CURRENT_DATE
            )"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS lecturers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                hire_date TEXT,
                department TEXT
            )"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                lecturer_id INTEGER,
                FOREIGN KEY (lecturer_id) REFERENCES lecturers (id)
            )"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                grade REAL,
                assignment_id INTEGER,
                student_id INTEGER,
                FOREIGN KEY (assignment_id) REFERENCES assignments (id),
                FOREIGN KEY (student_id) REFERENCES students (id)
            )"""
        )
        
        cursor.execute(''' 
         CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
         ''')
        print("تم إنشاء جدول المعلمين بنجاح.")  # تأكيد

        self.conn.commit()

    def close(self):
        self.conn.close()

# دالة للتحقق من وجود جدول المعلمين
def check_table_exists():
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='teachers';")
    table_exists = cursor.fetchone() is not None

    if table_exists:
        print("جدول المعلمين موجود.")
    else:
        print("جدول المعلمين غير موجود.")

    conn.close()

# استخدام Datamanager والتحقق من الجداول
dm = Datamanager()
check_table_exists()
