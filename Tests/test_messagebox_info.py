from PySide6.QtWidgets import QMessageBox, QApplication
from PySide6.QtGui import QColor


class CustomMessageBox(QMessageBox):
    def __init__(self, icon, title, text, parent=None):
        super().__init__(parent)
        self.setIcon(icon)
        self.setWindowTitle(title)
        self.setText(text)
        self.setStyleSheet("QLabel{ color: rgb(255, 0, 0); }")


    def exec_(self):
        return super().exec_()


if __name__ == '__main__':
    app = QApplication([])
    message_box = CustomMessageBox(QMessageBox.Information, "Information", "This is a custom message box.")
    message_box.exec_()