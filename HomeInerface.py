from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Studentinterface import StudentApp 
from teacherinterface import  TeacherApp# تأكد من أن هذا هو الاسم الصحيح للملف


class CustomWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # إعداد النافذة بدون إطار مع حدود منحنية
        self.setWindowTitle("Project")
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

        # إعداد تخطيط أفقي لأزرار التحكم
        control_layout = QtWidgets.QHBoxLayout()
        control_layout.setContentsMargins(5, 5, 5, 5)  # تعديل الهوامش لتكون صغيرة
        control_layout.setSpacing(10)

        # زر الإغلاق
        close_button = QtWidgets.QPushButton(self)
        close_button.setFixedSize(24, 24)  # تصغير حجم الزر
        close_button.setIcon(QtGui.QIcon('images/ex.png'))
        close_button.setIconSize(QtCore.QSize(16, 16))  # تعيين حجم الأيقونة
        close_button.setStyleSheet("""
            QPushButton {
                border-radius: 12px;
                background-color: red;
                border: none;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)
        close_button.setToolTip("Close")
        close_button.clicked.connect(self.close)
        control_layout.addWidget(close_button, alignment=QtCore.Qt.AlignLeft)

        # زر التصغير
        minimize_button = QtWidgets.QPushButton(self)
        minimize_button.setFixedSize(24, 24)  # تصغير حجم الزر
        minimize_button.setIcon(QtGui.QIcon('images/re.png'))
        minimize_button.setIconSize(QtCore.QSize(16, 16))  # تعيين حجم الأيقونة
        minimize_button.setStyleSheet("""
            QPushButton {
                border-radius: 12px;
                background-color: yellow;
                border: none;
            }
            QPushButton:hover {
                background-color: lightyellow;
            }
        """)
        minimize_button.setToolTip("Minimize")
        minimize_button.clicked.connect(self.showMinimized)
        control_layout.addWidget(minimize_button, alignment=QtCore.Qt.AlignLeft)

        # زر التكبير/التصغير
        self.maximized = False  # متغير لتتبع حالة التكبير
        self.maximize_button = QtWidgets.QPushButton(self)
        self.maximize_button.setFixedSize(24, 24)  # تصغير حجم الزر
        self.maximize_button.setIcon(QtGui.QIcon('images/zoom.png'))
        self.maximize_button.setIconSize(QtCore.QSize(16, 16))  # تعيين حجم الأيقونة
        self.maximize_button.setStyleSheet("""
            QPushButton {
                border-radius: 12px;
                background-color: green;
                border: none;
            }
            QPushButton:hover {
                background-color: darkgreen;
            }
        """)
        self.maximize_button.setToolTip("Maximize/Restore")
        self.maximize_button.clicked.connect(self.toggle_maximize_restore)
        control_layout.addWidget(self.maximize_button, alignment=QtCore.Qt.AlignLeft)

        # إعداد واجهة لأزرار التحكم
        control_widget = QtWidgets.QWidget(self)
        control_widget.setLayout(control_layout)
        control_widget.setFixedHeight(40)  # تحديد ارتفاع شريط التحكم
        control_widget.setFixedWidth(100)  # تحديد عرض شريط التحكم ليكون متناسب مع الأزرار
        control_widget.move(10, 10)  # ضبط مكان شريط التحكم في الأعلى يسار الشاشة

        # إعداد تخطيط عمودي للأزرار الرئيسية (إضافة، حذف، خروج)
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.setContentsMargins(20, 20, 20, 20)
        button_layout.setSpacing(20)
        button_layout.setAlignment(QtCore.Qt.AlignCenter)

        # زر "Add Student"
        button1 = QtWidgets.QPushButton('Add Student')
        button1.clicked.connect(self.open_student_app)  # ربط الزر بفتح واجهة الطالب
        button1.setStyleSheet("""
            QPushButton {
                padding: 15px 30px;
                border: 2px solid transparent;
                border-radius: 8px;
                font-size: 18px;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 10px;
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
        button_layout.addWidget(button1)

        # زر "Remove Student"
        button2 = QtWidgets.QPushButton('Add Teacher')
        button2.clicked.connect(self.open_teacher_app)  # ربط الزر بفتح واجهة المعلم
        button2.setStyleSheet("""
            QPushButton {
                padding: 15px 30px;
                border: 2px solid transparent;
                border-radius: 8px;
                font-size: 18px;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 10px;
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
        button_layout.addWidget(button2)

        # زر الخروج
        exit_button = QtWidgets.QPushButton('Exit')
        exit_button.setStyleSheet("""
            QPushButton {
                padding: 15px 30px;
                border: 2px solid transparent;
                border-radius: 8px;
                font-size: 18px;
                cursor: pointer;
                transition: all 0.3s ease;
                margin: 10px;
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
        exit_button.clicked.connect(sys.exit)
        button_layout.addWidget(exit_button)

        # إعداد تخطيط رئيسي للواجهة
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

        # تمكين المستخدم من سحب النافذة بدون إطار
        self.oldPos = self.pos()

        # وضع النافذة في منتصف الشاشة عند الفتح
        screen_geometry = QtWidgets.QApplication.primaryScreen().availableGeometry()
        window_size = self.size()
        x = (screen_geometry.width() - window_size.width()) // 2
        y = (screen_geometry.height() - window_size.height()) // 2
        self.move(x, y)

    def open_student_app(self):
        """Open the Student Application."""
        self.student_app = StudentApp(self.show)  # Pass the return function to StudentApp
        self.student_app.show()  # Show the StudentApp
        self.close()

    def open_teacher_app(self):
        self.teacher_app = TeacherApp(self.show)  # Pass the return function to TeacherApp
        self.teacher_app.show()  # Show the TeacherApp
        self.close()

    def toggle_maximize_restore(self):
        """وظيفة لتكبير النافذة إذا لم تكن مكبرة، وتصغيرها إلى نصف حجم الشاشة إذا كانت مكبرة"""
        if not self.maximized:
            self.showMaximized()  # تكبير النافذة بالكامل
            self.maximized = True
        else:
            screen_geometry = QtWidgets.QApplication.primaryScreen().availableGeometry()
            self.setGeometry(
                screen_geometry.width() // 4, screen_geometry.height() // 4,
                screen_geometry.width() // 2, screen_geometry.height() // 2
            )  # تصغير النافذة إلى نصف حجم الشاشة
            self.maximized = False

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CustomWindow()
    window.show()
    sys.exit(app.exec_())
