from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from Datamanager import Datamanager
from assignments import Assignment

class AddAssignmentDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("إضافة واجب")
        self.setGeometry(200, 200, 300, 200)

        self.title_label = QLabel("عنوان الواجب:")
        self.title_input = QLineEdit()

        self.details_label = QLabel("تفاصيل الواجب:")
        self.details_input = QLineEdit()

        self.add_button = QPushButton("إضافة")
        self.add_button.clicked.connect(self.add_assignment)

        self.cancel_button = QPushButton("إلغاء")
        self.cancel_button.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)
        layout.addWidget(self.details_label)
        layout.addWidget(self.details_input)
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

    def add_assignment(self):
        title = self.title_input.text()
        details = self.details_input.text()
        if title and details:  # تحقق من عدم كون الحقول فارغة
            # يمكن إضافة الكود لإضافة الواجب في هذه النقطة
            self.accept()
