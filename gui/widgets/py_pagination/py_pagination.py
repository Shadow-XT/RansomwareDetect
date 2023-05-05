from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QComboBox, QSpacerItem

from gui.widgets import PyPushButton, PyLineEdit


class PyPagination(QWidget):
    page_changed = Signal()
    # per_page_changed = Signal()

    def __init__(self, total_items, items_per_page=10, themes=None):
        super().__init__()

        self.total_items = total_items
        self.items_per_page = items_per_page
        self.current_page = 1
        self.total_pages = (total_items + items_per_page - 1) // items_per_page

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.first_button = PyPushButton(
            text="首页",
            radius=8,
            color=themes["app_color"]["text_foreground"],
            bg_color=themes["app_color"]["dark_one"],
            bg_color_hover=themes["app_color"]["dark_three"],
            bg_color_pressed=themes["app_color"]["dark_four"]
        )
        self.previous_button = PyPushButton(
            text="上一页",
            radius=8,
            color=themes["app_color"]["text_foreground"],
            bg_color=themes["app_color"]["dark_one"],
            bg_color_hover=themes["app_color"]["dark_three"],
            bg_color_pressed=themes["app_color"]["dark_four"]
        )
        self.next_button = PyPushButton(
            text="下一页",
            radius=8,
            color=themes["app_color"]["text_foreground"],
            bg_color=themes["app_color"]["dark_one"],
            bg_color_hover=themes["app_color"]["dark_three"],
            bg_color_pressed=themes["app_color"]["dark_four"]
        )
        self.last_button = PyPushButton(
            text="尾页",
            radius=8,
            color=themes["app_color"]["text_foreground"],
            bg_color=themes["app_color"]["dark_one"],
            bg_color_hover=themes["app_color"]["dark_three"],
            bg_color_pressed=themes["app_color"]["dark_four"]
        )
        self.jump_button = PyPushButton(
            text="跳转到",
            radius=8,
            color=themes["app_color"]["text_foreground"],
            bg_color=themes["app_color"]["dark_one"],
            bg_color_hover=themes["app_color"]["dark_three"],
            bg_color_pressed=themes["app_color"]["dark_four"]
        )
        self.txt_page = PyLineEdit(
            text="",
            place_holder_text="页数",
            radius=8,
            border_size=2,
            color=themes["app_color"]["text_foreground"],
            selection_color=themes["app_color"]["white"],
            bg_color=themes["app_color"]["dark_one"],
            bg_color_active=themes["app_color"]["dark_three"],
            context_color=themes["app_color"]["context_color"]
        )

        self.page_label = QLabel("")
        self.page_label.setAlignment(Qt.AlignCenter)
        self.page_label.setStyleSheet("font-size: 18px")
        # self.per_page_combo = QComboBox()

        # self.per_page_combo.addItem("10", 10)
        # self.per_page_combo.addItem("20", 20)
        # self.per_page_combo.addItem("50", 50)

        # layout.addWidget(QLabel("每页显示:"))
        # layout.addWidget(self.per_page_combo)
        self.first_button.setFixedSize(80, 40)
        self.previous_button.setFixedSize(80, 40)
        self.page_label.setFixedSize(160, 40)
        self.next_button.setFixedSize(80, 40)
        self.last_button.setFixedSize(80, 40)
        self.jump_button.setFixedSize(80, 40)
        self.txt_page.setFixedSize(70, 40)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.first_button)
        layout.addWidget(self.previous_button)
        layout.addWidget(self.page_label)
        layout.addWidget(self.next_button)
        layout.addWidget(self.last_button)
        layout.addWidget(self.jump_button)
        layout.addWidget(self.txt_page)

        self.update_controls()

        # self.first_button.clicked.connect(self.go_to_first)
        # self.previous_button.clicked.connect(self.go_to_previous)
        # self.next_button.clicked.connect(self.go_to_next)
        # self.last_button.clicked.connect(self.go_to_last)
        # self.jump_button.clicked.connect(self.go_to_jump)
        # self.per_page_combo.currentIndexChanged.connect(self.per_page_changed)

    def update_controls(self):
        self.page_label.setText(f"第 {self.current_page} / {self.total_pages} 页")

        if self.current_page == 1:
            self.first_button.setEnabled(False)
            self.previous_button.setEnabled(False)
        else:
            self.first_button.setEnabled(True)
            self.previous_button.setEnabled(True)

        if self.current_page == self.total_pages:
            self.next_button.setEnabled(False)
            self.last_button.setEnabled(False)
        else:
            self.next_button.setEnabled(True)
            self.last_button.setEnabled(True)

    @property
    def current_offset(self):
        return (self.current_page - 1) * self.items_per_page

    @property
    def current_limit(self):
        return self.items_per_page

        # start_row = (self.current_page - 1) * self.items_per_page + 1
        # end_row = min(start_row + self.items_per_page - 1, self.total_items)
        # self.page_label.setText(f"第 {self.current_page} / {self.total_pages} 页 （{start_row} 到 {end_row} 行）")

    # def go_to_first(self):
    #     self.current_page = 1
    #     self.update_controls()
    #     self.page_changed.emit()
    #
    # def go_to_previous(self):
    #     self.current_page -= 1
    #     self.update_controls()
    #     self.page_changed.emit()
    #
    # def go_to_next(self):
    #     self.current_page += 1
    #     self.update_controls()
    #     self.page_changed.emit()
    #
    # def go_to_last(self):
    #     self.current_page = self.total_pages
    #     self.update_controls()
    #     self.page_changed.emit()

    # def _per_page_changed(self, index):
    #     self.items_per_page = self.per_page_combo.currentData()
    #     self.total_pages = (self.total_items + self.items_per_page - 1) // self.items_per_page
    #     self.current_page = 1
    #     self.update_controls()
    #     self.per_page_changed.emit()


