import sys
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QInputDialog, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

class AssignmentsInterface(QWidget):
    def __init__(self, teacher_name, assignments):
        super().__init__()
        self.setWindowTitle(f"وظائف {teacher_name}")
        self.setGeometry(200, 200, 600, 400)  # زيادة الحجم قليلاً

        layout = QVBoxLayout(self)

        # عنوان المعلم
        title_label = QLabel(f"وظائف المعلم: {teacher_name}")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title_label, alignment=Qt.AlignCenter)

        self.assignments_table = QTableWidget()
        self.assignments_table.setColumnCount(3)
        self.assignments_table.setHorizontalHeaderLabels(["الوظيفة", "الدرجة", "تعديل"])
        self.assignments_table.horizontalHeader().setStretchLastSection(True)  # لضبط اتساع الأعمدة

        for assignment in assignments:
            self.add_assignment_row(assignment)

        layout.addWidget(self.assignments_table)

        # زر إضافة وظيفة
        self.add_assignment_button = QPushButton("إضافة وظيفة")
        self.add_assignment_button.setStyleSheet("""
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
        self.add_assignment_button.clicked.connect(self.open_add_assignment_dialog)  # يجب تنفيذ وظيفة لإضافة وظيفة جديدة
        layout.addWidget(self.add_assignment_button, alignment=Qt.AlignCenter)  # توسيط الزر في الأسفل

        self.setLayout(layout)

    def add_assignment_row(self, assignment):
        row_position = self.assignments_table.rowCount()
        self.assignments_table.insertRow(row_position)

        # إضافة بيانات الوظيفة
        self.assignments_table.setItem(row_position, 0, QTableWidgetItem(assignment['name']))
        self.assignments_table.setItem(row_position, 1, QTableWidgetItem(str(assignment['grade'])))

        # زر تعديل الدرجة
        edit_button = QPushButton("تعديل")
        edit_button.setStyleSheet("""
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
        edit_button.clicked.connect(lambda: self.edit_grade(row_position))
        self.assignments_table.setCellWidget(row_position, 2, edit_button)

    def edit_grade(self, row_position):
        grade_item = self.assignments_table.item(row_position, 1)
        new_grade, ok = QInputDialog.getInt(self, "تعديل الدرجة", "أدخل الدرجة الجديدة:", int(grade_item.text()))
        if ok:
            grade_item.setText(str(new_grade))

    def open_add_assignment_dialog(self):
        # هنا يمكنك إضافة كود فتح حوار لإضافة وظيفة جديدة
        pass
