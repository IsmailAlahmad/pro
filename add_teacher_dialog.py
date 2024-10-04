import sqlite3
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class AddTeacherDialog(QDialog):
    def __init__(self, parent, database_path):
        super().__init__(parent)
        self.setWindowTitle("إضافة معلم")
        self.setGeometry(200, 200, 300, 200)

        self.name_label = QLabel("الاسم:")
        self.name_input = QLineEdit()

        self.email_label = QLabel("البريد الإلكتروني:")
        self.email_input = QLineEdit()

        self.add_button = QPushButton("إضافة")
        self.add_button.clicked.connect(self.add_teacher)

        self.cancel_button = QPushButton("إلغاء")
        self.cancel_button.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        # تصميم الأزرار
        self.add_button.setStyleSheet(""" 
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.cancel_button.setStyleSheet(""" 
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)

        # إعداد قاعدة البيانات
        self.database_path = database_path
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()

    def add_teacher(self):
         name = self.name_input.text()
         email = self.email_input.text()
    
         print(f"الاسم المدخل: {name}, البريد الإلكتروني المدخل: {email}")  # طباعة البيانات المدخلة

         if name and email:  # تحقق من عدم كون الحقول فارغة
             try:
            # إضافة المعلم إلى قاعدة البيانات
                   self.cursor.execute('''INSERT INTO teachers (name, email) VALUES (?, ?)''', (name, email))
                   self.connection.commit()

            # إضافة المعلم إلى الجدول في الواجهة الرئيسية
                   self.parent().add_teacher_row(name, email)
                   self.accept()
             except sqlite3.IntegrityError:
                    QMessageBox.warning(self, "تحذير", "البريد الإلكتروني مستخدم بالفعل.")
             except sqlite3.Error as e:
                   QMessageBox.critical(self, "خطأ", f"فشل إضافة المعلم: {e}")
                   print(f"خطأ: {e}")  # طباعة رسالة الخطأ
         else:
            QMessageBox.warning(self, "تحذير", "يرجى ملء جميع الحقول.")

    def closeEvent(self, event):
        # إغلاق الاتصال بقاعدة البيانات عند إغلاق الحوار
        self.connection.close()
        event.accept()
