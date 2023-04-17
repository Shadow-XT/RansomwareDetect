import os.path
import sys
from gui.core.json_themes import Themes
from gui.widgets import PyTableViewPandas
import pandas as pd
from qt_core import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 200)
        self.vlayout = QVBoxLayout()
        themespath = Themes()
        themes = themespath.items

        self.table = PyTableViewPandas(color=themes["app_color"]["text_foreground"],
                                       selection_color=themes["app_color"]["context_color"],
                                       bg_color=themes["app_color"]["bg_two"],
                                       header_horizontal_color=themes["app_color"]["dark_two"],
                                       header_vertical_color=themes["app_color"]["bg_three"],
                                       bottom_line_color=themes["app_color"]["bg_three"],
                                       grid_line_color=themes["app_color"]["bg_one"],
                                       scroll_bar_bg_color=themes["app_color"]["bg_one"],
                                       scroll_bar_btn_color=themes["app_color"]["dark_four"],
                                       context_color=themes["app_color"]["context_color"]
                                       )
        self.vlayout.addWidget(self.table)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.table.setVerticalHeader()
        data = pd.DataFrame([
            ['John', 30, 'New York'],
            ['Jane', 25, 'Paris'],
            ['Bob', 40, 'London'],
            ['Alice', 35, 'Tokyo'],
            ['Tom', 50, 'Beijing'],
            ['Jack', 45, 'Shanghai'],
            ['Lily', 20, 'Shenzhen'],
        ], columns=['姓名', '年龄', '城市'])
        # self.model.setItemData()
        self.table.setModel(data)
        self.setCentralWidget(self.table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
