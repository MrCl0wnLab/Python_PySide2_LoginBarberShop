import sys
from ui_Formlogin import Ui_MainWindow
from assets import files

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # CREATE DROP SHADOW EFFECT
        self.shadow = self.set_drop_shadow()

        # SET DROP SHADOW EFFECT IN FRAME
        self.ui.frame_Shadow.setGraphicsEffect(self.shadow)

        # SET FUNCTION CLICK IN BUTTONS
        self.ui.pushButton_Exit.clicked.connect(self.click_exit)
        self.ui.pushButton_Login.clicked.connect(self.click_login)

        # ENABLE MODE PASSWORD IN LINE EDIT
        self.ui.lineEdit_Password.setEchoMode(QLineEdit.Password)

        # SET MOVE WINDOW
        def move_window(event):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.drag_pos)
                self.drag_pos = event.globalPos()
                event.accept()

        # ENABLE MOUSE MOVE FORM
        self.ui.frame_TopBar.mouseMoveEvent = move_window
        self.ui.frame_Shadow.mouseMoveEvent = move_window
        
        # SHOW FORM
        self.show()
        
    def set_drop_shadow(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        return self.shadow

    def click_exit(self):
        print("click button close")
        self.close()

    def click_login(self):
        print("click button login")

    def mousePressEvent(self, event):
        self.drag_pos = event.globalPos()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass
