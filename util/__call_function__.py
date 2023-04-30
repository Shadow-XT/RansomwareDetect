from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow

from gui.widgets import PyMessageBoxSingle


def __call_msgbox__(title, text, win: QMainWindow, icon=None, font_size=14):
    if icon is None:
        icon = win
    msg = PyMessageBoxSingle(icon, title, text,
                             color=win.themes["app_color"]["dark_four"],
                             selection_color=win.themes["app_color"]["white"],
                             bg_color=win.themes["app_color"]["dark_four"],
                             text_color=win.themes["app_color"]["text_foreground"],
                             btn_color=win.themes["app_color"]["text_foreground"],
                             btn_bg_color=win.themes["app_color"]["dark_one"],
                             btn_bg_color_hover=win.themes["app_color"]["dark_three"],
                             btn_bg_color_pressed=win.themes["app_color"]["dark_four"]
                             )
    msg.setFont(QFont("微软雅黑", font_size))
    msg.exec()
