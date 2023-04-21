from qt_core import *


class PyMessageBoxConfirm(QMessageBox):
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
                 buttons: dict[QMessageBox.ButtonRole, str] = None,
                 width=(500, 250)):
        super().__init__(icon)
        self.setMinimumWidth(width[0])

        self.setMaximumWidth(width[1])
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # self.setIcon(icon)
        self.setWindowTitle(title)
        self.setText(text)
        self.btn_dict: dict[str, QPushButton] = {}
        if buttons is not None:
            for button in buttons.items():
                self.btn_dict[button[1]] = self.addButton(button[1], button[0])
                # self.btn_dict[button[1]] = self.addButton(button[1], button[0])
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
    min-width: 6em;
    min-height: 3em;
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
