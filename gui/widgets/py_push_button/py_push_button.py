# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style1 = '''
QPushButton {{
	border: none;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''

style2 = '''
QPushButton {{
	border: none;
	height: {_heigh};
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton(QPushButton):
    def __init__(
            self,
            text,
            radius,
            color,
            bg_color,
            bg_color_hover,
            bg_color_pressed,
            heigh=None,
            parent=None,
    ):
        super().__init__()

        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        if heigh is None:
            custom_style = style1.format(
                _color=color,
                _radius=radius,
                _bg_color=bg_color,
                _bg_color_hover=bg_color_hover,
                _bg_color_pressed=bg_color_pressed
            )
            self.setStyleSheet(custom_style)
        else:
            custom_style = style2.format(
                _heigh=heigh,
                _color=color,
                _radius=radius,
                _bg_color=bg_color,
                _bg_color_hover=bg_color_hover,
                _bg_color_pressed=bg_color_pressed
            )
            self.setStyleSheet(custom_style)
