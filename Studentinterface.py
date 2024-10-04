from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Datamanager import Datamanager
from Student import Student

class AddStudentDialog(QtWidgets.QDialog):
    def __init__(self, db_manager, parent=None):
        super().__init__(parent)
        self.db_manager = db_manager
        
        self.setWindowTitle("إضافة طالب")
        self.setGeometry(500, 300, 300, 200)

        # إنشاء تخطيط
        layout = QtWidgets.QVBoxLayout()

        # إدخال الاسم الأول
        self.first_name_input = QtWidgets.QLineEdit(self)
        self.first_name_input.setPlaceholderText("الاسم الأول")
        layout.addWidget(self.first_name_input)

        # إدخال الاسم الأخير
        self.last_name_input = QtWidgets.QLineEdit(self)
        self.last_name_input.setPlaceholderText("الاسم الأخير")
        layout.addWidget(self.last_name_input)

        # إدخال البريد الإلكتروني
        self.email_input = QtWidgets.QLineEdit(self)
        self.email_input.setPlaceholderText("البريد الإلكتروني")
        layout.addWidget(self.email_input)

        # إدخال تاريخ الميلاد
        self.dob_input = QtWidgets.QLineEdit(self)
        self.dob_input.setPlaceholderText("تاريخ الميلاد (YYYY-MM-DD)")
        layout.addWidget(self.dob_input)

        # زر الإضافة
        self.add_button = QtWidgets.QPushButton("إضافة")
        self.add_button.clicked.connect(self.add_student)
        layout.addWidget(self.add_button)

        # تعيين التخطيط
        self.setLayout(layout)

    def add_student(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        email = self.email_input.text()
        date_of_birth = self.dob_input.text()

        if first_name and last_name and email and date_of_birth:
            new_student = Student(first_name, last_name, email, date_of_birth)
            new_student.save_to_db(self.db_manager)  # حفظ الطالب في قاعدة البيانات
            self.accept()  # إغلاق النافذة بعد الإضافة
        else:
            QtWidgets.QMessageBox.warning(self, "خطأ", "يرجى ملء جميع الحقول.")

class StudentApp(QtWidgets.QWidget):
    def __init__(self, return_to_main):
        super().__init__()

        self.return_to_main = return_to_main
        self.db_manager = Datamanager()  # إنشاء كائن مدير قاعدة البيانات

        # إعداد النافذة مع إعدادات مشابهة للواجهة الرئيسية
        self.setWindowTitle("Student List")
        self.setWindowIcon(QtGui.QIcon('images/th.jpeg'))
        self.setGeometry(400, 200, 800, 600)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # إزالة إطار النافذة
        self.setMinimumSize(400, 300)  # ضبط أقل حجم يمكن الوصول له
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # لإضافة شفافية للخلفية

        # إعداد الخلفية باستخدام QLabel
        self.background_label = QtWidgets.QLabel(self)
        background_pixmap = QtGui.QPixmap('images/download.jpeg')
        self.background_label.setPixmap(background_pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.rect())  # ضبط الخلفية على حجم النافذة

        # إعداد تخطيط عمودي لعناصر الواجهة
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # شريط البحث
        search_layout = QtWidgets.QHBoxLayout()
        search_label = QtWidgets.QLabel("Search by Birthdate (YYYY-MM-DD):")
        self.search_input = QtWidgets.QLineEdit()

        # زر البحث مع تنسيق مشابه للأزرار الرئيسية
        search_button = QtWidgets.QPushButton("Search")
        search_button.setStyleSheet(""" 
            QPushButton {
                padding: 5px 10px;
                border: 2px solid transparent;
                border-radius: 8px;
                font-size: 14px;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 5px;
                color: white;
                font-weight: bold;
                background-color: #008CBA;
            }
            QPushButton:hover {
                transform: scale(1.1);
                border-color: white;
            }
            QPushButton:pressed {
                background-color: #005f73;
            }
        """)
        search_button.clicked.connect(self.search_student)

        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)

        main_layout.addLayout(search_layout)

        # زر الإضافة
        add_student_button = QtWidgets.QPushButton("إضافة طالب")
        add_student_button.setStyleSheet(""" 
            QPushButton {
                padding: 5px 10px;
                border: 2px solid transparent;
                border-radius: 8px;
                font-size: 14px;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 5px;
                color: white;
                font-weight: bold;
                background-color: #4CAF50;
            }
            QPushButton:hover {
                transform: scale(1.1);
                border-color: white;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """)
        add_student_button.clicked.connect(self.open_add_student_dialog)
        search_layout.addWidget(add_student_button)

        # زر العودة الذي يظهر دائمًا بجانب البحث
        return_search_button = QtWidgets.QPushButton("Return to Main")
        return_search_button.setStyleSheet(""" 
            QPushButton {
                padding: 5px 10px;
                border: 2px solid transparent;
                border-radius: 8px;
                font-size: 14px;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 5px;
                color: white;
                font-weight: bold;
                background-color: #f44336;
            }
            QPushButton:hover {
                transform: scale(1.1);
                border-color: white;
            }
            QPushButton:pressed {
                background-color: #c62828;
            }
        """)
        return_search_button.clicked.connect(self.return_to_main_interface)
        search_layout.addWidget(return_search_button)

        # الجدول لعرض الطلاب
        self.student_table = QtWidgets.QTableWidget(self)
        self.student_table.setColumnCount(3)
        self.student_table.setHorizontalHeaderLabels(["Name", "Birthdate", "Delete"])
        self.student_table.horizontalHeader().setStretchLastSection(True)
        self.student_table.setStyleSheet("""
            QTableWidget {
                background-color: rgba(255, 255, 255, 180);  # خلفية شفافة قليلاً
                border-radius: 10px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 4px;
                border-radius: 5px;
            }
        """)

        main_layout.addWidget(self.student_table)

        # تعبئة الجدول ببيانات الطلاب من قاعدة البيانات
        self.load_students()

        # زر العودة مع تنسيق مصغر
        back_button = QtWidgets.QPushButton("Back")
        back_button.setStyleSheet(""" 
            QPushButton {
                padding: 5px 10px;
                border: 2px solid transparent;
                border-radius: 8px;
                font-size: 14px;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 5px;
                color: white;
                font-weight: bold;
                background-color: #f44336;
            }
            QPushButton:hover {
                transform: scale(1.1);
                border-color: white;
            }
            QPushButton:pressed {
                background-color: #c62828;
            }
        """)
        back_button.clicked.connect(self.return_to_main_interface)
        main_layout.addWidget(back_button)

        # إعداد سحب النافذة بدون إطار
        self.oldPos = self.pos()

    def load_students(self, students=None):
        """Loads the student list into the table"""
        if students is None:
            students = Student.get_all_students(self.db_manager)  # جلب جميع الطلاب من قاعدة البيانات

        self.student_table.setRowCount(len(students))

        for row, student in enumerate(students):
            name_item = QtWidgets.QTableWidgetItem(f"{student.first_name} {student.last_name}")
            birthdate_item = QtWidgets.QTableWidgetItem(str(student.date_of_birth))

            # زر الحذف مع تنسيق مصغر
            delete_button = QtWidgets.QPushButton("Delete")
            delete_button.setStyleSheet(""" 
                QPushButton {
                    padding: 3px 6px;
                    border: 2px solid transparent;
                    border-radius: 8px;
                    font-size: 12px;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    color: white;
                    background-color: #f44336;
                }
                QPushButton:hover {
                    transform: scale(1.1);
                    border-color: white;
                }
                QPushButton:pressed {
                    background-color: #c62828;
                }
            """)
            delete_button.clicked.connect(lambda ch, r=row: self.delete_student(student.id))  # تمرير ID الطالب

            self.student_table.setItem(row, 0, name_item)
            self.student_table.setItem(row, 1, birthdate_item)
            self.student_table.setCellWidget(row, 2, delete_button)

    def search_student(self):
        """Filters the student list based on the search input"""
        search_term = self.search_input.text()
        if search_term:  # تأكد من أن حقل الإدخال ليس فارغًا
            students = Student.search_students_by_dob(self.db_manager, search_term, search_term)  # البحث بناءً على تاريخ الميلاد
            self.load_students(students)
        else:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a birthdate to search.")

    def delete_student(self, student_id):
        """Deletes a student from the list"""
        Student.delete_from_db(self.db_manager, student_id)  # حذف الطالب من قاعدة البيانات
        self.load_students()  # إعادة تحميل الطلاب

    def return_to_main_interface(self):
        """Returns to the main interface"""
        self.return_to_main()
        self.close()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def open_add_student_dialog(self):
        """Opens the dialog to add a new student"""
        dialog = AddStudentDialog(self.db_manager, self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_students()  # Reload the student list after adding

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StudentApp(lambda: print("Returning to main interface..."))
    window.show()
    sys.exit(app.exec_())
