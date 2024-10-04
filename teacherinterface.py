import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout,
    QHeaderView, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from AreYourSureinterface import AreYouSureInterface  # استيراد واجهة التأكيد
from assignments_interface import AssignmentsInterface  # استيراد واجهة الوظائف من الملف الجديد
from add_teacher_dialog import AddTeacherDialog
from add_assignment_dialog import AddAssignmentDialog
from Lecturer import Lecturer

class TeacherApp(QWidget):
    def __init__(self, return_to_main):
        super().__init__()
        self.return_to_main = return_to_main  # حفظ دالة الرجوع

        # إعداد الواجهة
        self.setWindowTitle("إدارة المعلمين")
        self.setGeometry(100, 100, 800, 600)

        # إعداد الخلفية
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("images/download.jpeg"))
        self.background_label.setScaledContents(True)  # جعل الصورة تتناسب مع حجم الواجهة
        self.background_label.resize(self.size())  # تعيين حجم الصورة ليكون بحجم النافذة

        # إنشاء مربع البحث
        self.search_label = QLabel("بحث عن معلم (بالإيميل أو الاسم):")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("أدخل البريد الإلكتروني أو الاسم")
        self.search_input.setFixedWidth(int(self.width() * 0.50))  # ضبط العرض ليكون 50% من العرض
        self.search_input.setFixedHeight(30)  # تقليل الارتفاع
        self.search_input.setStyleSheet("margin-left: 0px;")  # وضعه على أقصى اليسار

        # زر إضافة معلم
        self.add_teacher_button = QPushButton("إضافة معلم")
        self.add_teacher_button.setStyleSheet(""" 
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 10px;
                width: 150px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.add_teacher_button.clicked.connect(self.open_add_teacher_dialog)

        # زر البحث
        self.search_button = QPushButton("بحث")
        self.search_button.setStyleSheet(""" 
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 10px;
                width: 150px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.search_button.clicked.connect(self.search_teacher)  # ربط الزر بدالة البحث

        # زر الرجوع
        self.back_button = QPushButton("رجوع")
        self.back_button.setStyleSheet(""" 
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 10px;
                width: 150px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        self.back_button.clicked.connect(self.return_to_main)  # ربط الزر بالوظيفة

        # إنشاء جدول لعرض بيانات المعلم
        self.teacher_table = QTableWidget()
        self.teacher_table.setColumnCount(5)  # اسم، إيميل، زر إضافة وظيفة، زر وظائف، زر حذف معلم
        self.teacher_table.setHorizontalHeaderLabels(["الاسم", "الإيميل", "إضافة وظيفة", "وظائف", "حذف معلم"])
        self.teacher_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # ضبط الجدول لعرض 6 صفوف فقط مع إمكانية التمرير
        self.teacher_table.setFixedHeight(180)
        self.teacher_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # ملء الجدول ببيانات افتراضية
        for i in range(10):
            self.add_teacher_row(f"معلم {i + 1}", f"teacher{i + 1}@school.com")

        # تصميم التخطيط
        layout = QVBoxLayout(self)
        search_layout = QHBoxLayout()

        # إضافة مسافة من الأعلى
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # إضافة العناصر بتنسيق مع الحواف
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)  # إضافة زر البحث
        search_layout.addWidget(self.add_teacher_button)
        search_layout.addWidget(self.back_button)  # إضافة زر الرجوع إلى التخطيط

        layout.addLayout(search_layout)
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))  # إضافة فراغ
        layout.addWidget(self.teacher_table)

        self.setLayout(layout)

    def resizeEvent(self, event):
        # تكبير الخلفية لتتناسب مع حجم النافذة عند تغيير الحجم
        self.background_label.resize(self.size())

    def add_teacher_row(self, name, email):
        row_position = self.teacher_table.rowCount()
        self.teacher_table.insertRow(row_position)

        # إضافة بيانات المعلم
        self.teacher_table.setItem(row_position, 0, QTableWidgetItem(name))
        self.teacher_table.setItem(row_position, 1, QTableWidgetItem(email))

        # زر إضافة واجب
        add_job_button = QPushButton("إضافة واجب")
        add_job_button.setStyleSheet(""" 
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 10px;
                padding: 4px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        add_job_button.clicked.connect(self.open_add_assignment_dialog)  # ربط الزر بفتح الحوار
        self.teacher_table.setCellWidget(row_position, 2, add_job_button)

        # زر وظائف
        jobs_button = QPushButton("وظائف")
        jobs_button.setStyleSheet(""" 
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-size: 10px;
                padding: 4px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #FB8C00;
            }
        """)
        jobs_button.clicked.connect(lambda: self.open_assignments_interface(name))  # ربط الزر بفتح واجهة الوظائف
        self.teacher_table.setCellWidget(row_position, 3, jobs_button)

        # زر حذف معلم مع أيقونة
        delete_teacher_button = QPushButton()
        delete_teacher_button.setIcon(QIcon("delete_icon.png"))  # إضافة الأيقونة
        delete_teacher_button.setStyleSheet(""" 
            QPushButton {
                background-color: #f44336;
                padding: 4px;
                border-radius: 8px;
                width: 50px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        delete_teacher_button.clicked.connect(lambda: self.confirm_delete_teacher(row_position))  # ربط الزر بوظيفة التأكيد
        self.teacher_table.setCellWidget(row_position, 4, delete_teacher_button)

    def confirm_delete_teacher(self, row_position):
        confirmation = AreYouSureInterface(on_confirm=lambda: self.delete_teacher(row_position))
        confirmation.setWindowModality(Qt.ApplicationModal)
        confirmation.exec_()

    def delete_teacher(self, row_position):
        self.teacher_table.removeRow(row_position)  # حذف الصف

    def open_add_teacher_dialog(self):
        dialog = AddTeacherDialog(self, "university.db")  # تأكد من تعديل مسار قاعدة البيانات
        dialog.exec_()


    def open_add_assignment_dialog(self):
        dialog = AddAssignmentDialog(self)
        dialog.exec_()

    def open_assignments_interface(self, teacher_name):
        # مثال على بيانات الوظائف، يمكنك استبدالها بالبيانات الحقيقية
        assignments = [
            {'name': 'وظيفة 1', 'grade': 90},
            {'name': 'وظيفة 2', 'grade': 85},
        ]
        assignments_interface = AssignmentsInterface(teacher_name, assignments)
        assignments_interface.show()  # استخدام show() بدلاً من exec_()

    def search_teacher(self):
       search_query = self.search_input.text()
       print(f"البحث عن: {search_query}")

    # قم بإفراغ الجدول أولاً
       self.teacher_table.setRowCount(0)

    # استدعاء دالة البحث من كلاس Lecturer
       db_manager = Datamanager()  # تأكد من أن لديك كائن Datamanager لفتح قاعدة البيانات
       lecturers = Lecturer.search_lecturers(db_manager, search_query)

    # تحقق من نوع lecturers وطباعة النتائج للتشخيص
       print(f"عدد المعلمين الذين تم العثور عليهم: {len(lecturers)}")  # تأكيد عدد المعلمين

    # أضف كل معلم تم العثور عليه إلى الجدول
       for lecturer in lecturers:
            print(f"إضافة معلم: {lecturer.first_name} {lecturer.last_name}")  # تأكيد إضافة المعلم
            self.add_teacher_row(lecturer.first_name + " " + lecturer.last_name, lecturer.email)

    # إذا لم يتم العثور على أي معلمين، يمكنك إظهار رسالة أو اتخاذ إجراء آخر
       if not lecturers:
          print("لم يتم العثور على أي معلمين.")

        # يمكنك هنا إضافة المنطق الخاص بك للبحث في الجدول

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TeacherApp(lambda: print("رجوع إلى الصفحة الرئيسية"))
    main_window.show()
    sys.exit(app.exec_())
