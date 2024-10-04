import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt

class AreYouSureInterface(QDialog):
    def __init__(self, on_confirm=None):
        super().__init__()
        self.on_confirm = on_confirm  # تخزين دالة الحذف
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Confirmation Page')
        self.setGeometry(100, 100, 400, 300)

        # إعداد الخلفية باستخدام صورة
        background_image = QPixmap('images/download.jpeg')
        background_image = background_image.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.setPalette(palette)

        # إعداد الحاوية الشفافة داخل النافذة
        container = QWidget(self)
        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.3); border-radius: 15px;")
        container.setFixedSize(300, 200)

        # إعداد النص داخل الحاوية
        label = QLabel('هل أنت متأكد من عملية الحذف؟', container)
        label.setStyleSheet("font-size: 16px; color: #343a40;")
        label.setAlignment(Qt.AlignCenter)

        # إعداد زر "نعم"
        yes_button = QPushButton('نعم', container)
        yes_button.setStyleSheet(""" 
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 15px; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        yes_button.clicked.connect(self.confirm_action)

        # إعداد زر "لا"
        no_button = QPushButton('لا', container)
        no_button.setStyleSheet(""" 
            QPushButton {
                background-color: #dc3545;
                color: white;
                border-radius: 15px; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        no_button.clicked.connect(self.reject_action)

        # ترتيب الأزرار بجانب بعضها البعض
        button_layout = QHBoxLayout()
        button_layout.addWidget(yes_button)
        button_layout.addWidget(no_button)

        # ترتيب جميع العناصر داخل الحاوية
        layout = QVBoxLayout(container)
        layout.addWidget(label)
        layout.addLayout(button_layout)
        layout.setAlignment(Qt.AlignCenter)

        # ضبط موضع الحاوية في منتصف النافذة
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(container)
        main_layout.setAlignment(Qt.AlignCenter)

    def confirm_action(self):
        # استدعاء رسالة التأكيد بنفس تصميم الواجهة
        self.show_confirmation_message('تم التأكيد', 'تم تأكيد عملية الحذف.')

    def reject_action(self):
        # استدعاء رسالة التأكيد بنفس تصميم الواجهة
        self.show_confirmation_message('تم الإلغاء', 'لم يتم حذف العنصر.')

    def show_confirmation_message(self, title, message):
        confirmation_dialog = QDialog(self)
        confirmation_dialog.setWindowTitle(title)
        confirmation_dialog.setGeometry(150, 150, 300, 150)

        # إعداد الخلفية باستخدام صورة
        background_image = QPixmap('images/download.jpeg')
        background_image = background_image.scaled(confirmation_dialog.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        confirmation_dialog.setPalette(palette)

        # إعداد الحاوية الشفافة داخل النافذة
        container = QWidget(confirmation_dialog)
        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.3); border-radius: 15px;")
        container.setFixedSize(280, 120)

        # إعداد النص داخل الحاوية
        label = QLabel(message, container)
        label.setStyleSheet("font-size: 16px; color: #343a40;")
        label.setAlignment(Qt.AlignCenter)

        # زر إغلاق
        close_button = QPushButton('إغلاق', container)
        close_button.setStyleSheet(""" 
            QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 15px; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0069d9;
            }
        """)
        close_button.clicked.connect(lambda: self.close_and_accept(confirmation_dialog))

        # ترتيب العناصر داخل الحاوية
        layout = QVBoxLayout(container)
        layout.addWidget(label)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)
        layout.setAlignment(Qt.AlignCenter)

        confirmation_dialog.exec_()  # عرض النافذة الجديدة

    def close_and_accept(self, confirmation_dialog):
        confirmation_dialog.close()  # أغلق واجهة التأكيد
        self.accept()  # أغلق واجهة AreYouSureInterface

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AreYouSureInterface()
    window.show()
    sys.exit(app.exec_())
