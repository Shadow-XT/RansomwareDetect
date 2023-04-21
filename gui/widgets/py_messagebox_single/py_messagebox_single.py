from qt_core import *


class PyMessageBoxSingle(QMessageBox):
    def __init__(self,
                 icon=None,
                 title=None,
                 text=None,
                 color="#FFF",
                 selection_color="#FFF",
                 bg_color="#333",
                 text_color="#FFFFFF",
                 btn_color=None,
                 btn_bg_color=None,
                 btn_bg_color_hover=None,
                 btn_bg_color_pressed=None,
                 width=(500, 250)):
        super().__init__(icon)
        self.setMinimumWidth(width[0])

        self.setMaximumWidth(width[1])
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # self.setIcon(icon)
        self.setWindowTitle(title)
        self.setText(text)
        self.addButton("确定", QMessageBox.YesRole)
        self.set_stylesheet(selection_color, bg_color, text_color, btn_color,
                            btn_bg_color, btn_bg_color_hover, btn_bg_color_pressed)

    def set_stylesheet(self,
                       selection_color,
                       bg_color,
                       text_color,
                       btn_color,
                       btn_bg_color,
                       btn_bg_color_hover,
                       btn_bg_color_pressed):
        style = f"""
QMessageBox {{
    background-color: {bg_color};
    selection-color: {selection_color};
}}
QMessageBox QLabel {{
    color: {text_color};
}}
QMessageBox QPushButton {{
    border-radius: 5px;
    color: {btn_color};	
    background-color: {btn_bg_color};
    min-width: 5em;
    min-height: 2em;
    font: bold 18px;
}}
QPushButton:hover {{
    background-color: {btn_bg_color_hover};
}}
QPushButton:pressed {{	
    background-color: {btn_bg_color_pressed};
}}
"""
        self.setStyleSheet(style)
