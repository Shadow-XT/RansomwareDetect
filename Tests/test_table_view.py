import os.path

from gui.core.json_themes import Themes
from gui.widgets import PyTableView
import pandas as pd
from qt_core import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 200)
        self.vlayout = QVBoxLayout()
        themespath = Themes()
        themes = themespath.items

        self.table = PyTableView(4,
                                 color=themes["app_color"]["text_foreground"],
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
        data = [
            [4, 9, 2],
            [1, 0, 0],
            [3, 5, 0],
            [3, 3, 2],
            [7, 8, 9],
        ]

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['年份', '上报情况', '上报时间', '附件上传', '操作'])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        self.model.appendRow([
            QStandardItem("2022"),
            QStandardItem("无"),
            QStandardItem("12-25"),
            QStandardItem("无")
        ])
        # self.model.setItemData()
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
