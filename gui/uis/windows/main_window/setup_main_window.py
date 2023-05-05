# 导入包和模块
from gui.widgets.py_pagination import PyPagination
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from .functions_main_window import *
import sys
import os

# 导入qt_core
from qt_core import *

# 导入设置
from gui.core.json_settings import Settings

# 导入主题映射
from gui.core.json_themes import Themes

# 导入PyOneDark的组件
from gui.widgets import *

# 加载主窗口UI
from .ui_main import *

# 导入主窗口会用到的函数
from .functions_main_window import *


# PY WINDOW
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # 设置主窗口
        # 从"gui\uis\main_window\ui_main.py"加载UI
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # 添加左列菜单栏
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",  # home菜单
            "btn_id": "btn_home",
            "btn_text": "首页",
            "btn_tooltip": "首页",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "icon_init.svg",  # 初始化设置文件菜单
            "btn_id": "btn_init",
            "btn_text": "配置诱饵文件",
            "btn_tooltip": "诱饵文件配置页面",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_database_2.svg",  # 数据库菜单
            "btn_id": "btn_database",
            "btn_text": "程序数据库",
            "btn_tooltip": "程序数据库页面",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_monitor.svg",  # 执行检测菜单
            "btn_id": "btn_run",
            "btn_text": "执行检测",
            "btn_tooltip": "执行检测页面",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_widgets.svg",  # 自定义组件显示菜单
            "btn_id": "btn_widgets",
            "btn_text": "自定义组件",
            "btn_tooltip": "自定义组件页面",
            "show_top": True,
            "is_active": False
        },
        # {
        #     "btn_icon": "icon_add_user.svg",
        #     "btn_id": "btn_add_user",
        #     "btn_text": "Add Users",
        #     "btn_tooltip": "Add users",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_file.svg",
        #     "btn_id": "btn_new_file",
        #     "btn_text": "New File",
        #     "btn_tooltip": "Create new file",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_folder_open.svg",
        #     "btn_id": "btn_open_file",
        #     "btn_text": "Open File",
        #     "btn_tooltip": "Open file",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_save.svg",
        #     "btn_id": "btn_save",
        #     "btn_text": "Save File",
        #     "btn_tooltip": "Save file",
        #     "show_top": True,
        #     "is_active": False
        # },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_info",
            "btn_text": "系统信息",
            "btn_tooltip": "打开信息页面",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_settings",
            "btn_text": "设置",
            "btn_tooltip": "打开设置页面",
            "show_top": False,
            "is_active": False
        }
    ]

    # 添加标题栏菜单
    add_title_bar_menus = [
        {
            "btn_icon": "icon_search.svg",
            "btn_id": "btn_search",
            "btn_tooltip": "Search",
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_top_settings",
            "btn_tooltip": "Top settings",
            "is_active": False
        }
    ]

    # 设置自定义组件中的自定义按钮
    # 获取当按钮被点击时的sender函数
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # 使用自定义参数设置主窗口
    def setup_gui(self):
        # 设置主窗口的标题
        self.setWindowTitle(self.settings["app_name"])

        # 不显示标题栏
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # 左侧菜单栏 / 左侧菜单栏中的按钮被点击或者释放时的链接的信号
        # 添加左侧菜单栏
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # 设置左边菜单按钮的信号
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # 标题栏 / 添加额外的按钮
        # 添加标题菜单栏
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # 设置信号
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # 添加标题
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # 设置左侧的信号
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # 设置初始化页面
        # 设置左侧和右侧的菜单
        MainFunctions.set_page(self, self.ui.load_pages.page_1_home)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>

        # 加载设置
        settings = Settings()
        self.settings = settings.items

        # 加载主题颜色
        themes = Themes()
        self.themes = themes.items

        # 左侧菜单栏
        # 按钮1
        self.left_btn_1 = PyPushButton(
            text="Btn 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        # 按钮2
        self.left_btn_2 = PyPushButton(
            text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        # 按钮3 使用默认的QPushButton
        self.left_btn_3 = QPushButton("Default QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        # 页面1
        #  页面1（主页） - 添加logo到主页
        self.logo_svg = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # 页面2（配置诱饵文件）
        self.ui.file_table = PyTableViewPandasWithButton(
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"],
            ui=self.ui
        )
        import pandas as pd
        init_data = pd.DataFrame([
        ], columns=['文件', '类型', '大小'])
        # self.model.setItemData()
        # self.file_table.setModel(data)
        # self.ui.file_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.load_pages.hlayout2_table.addWidget(self.ui.file_table)
        self.ui.file_table.setModel(init_data)
        self.ui.file_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.file_table.setColumnWidth(0, 500)
        # 将其它列设置为指定宽度
        self.ui.file_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.file_table.setColumnWidth(1, 230)
        self.ui.file_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.ui.file_table.setColumnWidth(2, 120)
        self.ui.file_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.file_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        colorx = self.themes["app_color"]["bg_three"]
        self.ui.file_table.verticalHeader().setStyleSheet(f'background-color: {colorx};')

        # self.ui.load_pages.hlayout2_table.setCentralWidget(self.file_table)
        # self.setCentralWidget(self.file_table)

        self.ui.btn_load_profile = PyPushButton(
            heigh="50px",
            text="加载配置",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.btn_save_profile = PyPushButton(
            heigh="50px",
            text="保存配置",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.btn_load_file = PyPushButton(
            heigh="50px",
            text="添加文件",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.btn_clear_file = PyPushButton(
            heigh="50px",
            text="清空文件",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.load_pages.hlayout2_button.addWidget(self.ui.btn_load_profile)
        self.ui.load_pages.hlayout2_button.addWidget(self.ui.btn_save_profile)
        self.ui.load_pages.hlayout2_button.addWidget(self.ui.btn_load_file)
        self.ui.load_pages.hlayout2_button.addWidget(self.ui.btn_clear_file)
        self.ui.load_pages.label_set_file.setStyleSheet("font-size: 25px")

        # 页面3（数据库设置）
        self.ui.lable_host = QLabel(text="主机:")
        self.ui.lable_host.setStyleSheet("font-size: 20px")
        self.ui.lable_port = QLabel(text="端口:")
        self.ui.lable_port.setStyleSheet("font-size: 20px")
        self.ui.txt_host = PyLineEdit(
            text="",
            place_holder_text="主机IP",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.ui.txt_host.setMinimumHeight(50)
        self.ui.txt_port = PyLineEdit(
            text="",
            place_holder_text="API端口",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.ui.txt_port.setMinimumHeight(50)
        self.ui.btn_load_url = PyPushButton(
            heigh="50px",
            text="加载链接",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"])
        self.ui.btn_load_url.setMinimumWidth(120)
        self.ui.btn_db_connect = PyPushButton(
            heigh="50px",
            text="测试链接",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"])
        self.ui.btn_db_connect.setMinimumWidth(120)
        self.ui.btn_save_url = PyPushButton(
            heigh="50px",
            text="保存链接",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"])
        self.ui.btn_save_url.setMinimumWidth(120)
        self.ui.btn_load_log = PyPushButton(
            heigh="50px",
            text="加载日志",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"])
        self.ui.btn_load_log.setMinimumWidth(120)
        self.ui.spacer_txt1 = QSpacerItem(10, 20)
        self.ui.spacer_txt2 = QSpacerItem(20, 20)
        self.ui.load_pages.label_database.setStyleSheet("font-size: 25px")
        # from qfluentwidgets.components import TableView
        # self.ui.database_table = TableView()
        self.ui.load_pages.hlayout3_connect.addWidget(self.ui.lable_host)
        self.ui.load_pages.hlayout3_connect.addWidget(self.ui.txt_host)
        self.ui.load_pages.hlayout3_connect.addItem(self.ui.spacer_txt1)
        self.ui.load_pages.hlayout3_connect.addWidget(self.ui.lable_port)
        self.ui.load_pages.hlayout3_connect.addWidget(self.ui.txt_port)
        self.ui.load_pages.hlayout3_connect.addItem(self.ui.spacer_txt2)
        self.ui.load_pages.hlayout3_connect.addWidget(self.ui.btn_load_url)
        self.ui.load_pages.hlayout3_connect.addWidget(self.ui.btn_db_connect)
        self.ui.load_pages.hlayout3_connect.addWidget(self.ui.btn_save_url)
        self.ui.load_pages.hlayout3_connect.addWidget(self.ui.btn_load_log)

        self.ui.database_table = PyTableViewPandasSingle(
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        data_database = pd.DataFrame(
            [],
            columns=["文件夹", "原文件名", "新文件名", "修改时间"]
        )
        self.ui.database_table.setModelX(data_database,vertical=[i for i in range(0, 10)])
        self.ui.database_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.database_table.setColumnWidth(0, 260)
        # 将其它列设置为指定宽度
        self.ui.database_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.database_table.setColumnWidth(1, 210)
        self.ui.database_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.ui.database_table.setColumnWidth(2, 330)
        self.ui.database_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.load_pages.hlayout3_loginfo.addWidget(self.ui.database_table)
        self.ui.pagination = PyPagination(0, 10, self.themes)
        self.ui.load_pages.hlayout3_pagination.addWidget(self.ui.pagination)
        self.ui.database_table.verticalHeader().setStyleSheet(f'background-color: {colorx};')
        self.ui.database_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.logCount = 0

        # 页面4（运行检测）
        # 添加运行表格
        self.ui.monitor_table = PyTableViewPandasSingle(
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # TODO: 需要完善
        data_monitor = pd.DataFrame(
            [],
            columns=["文件夹", "原文件名", "新文件名", "大小", "修改时间", "信息熵"]
        )
        # self.ui.run_table_model = MonitorTableModel(self.ui.run_table_data, self.ui.run_table_headers)
        self.ui.monitor_table.setModelX(data_monitor, floatRule=(5, 6))

        self.ui.monitor_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.monitor_table.setColumnWidth(0, 280)
        # 将其它列设置为指定宽度
        self.ui.monitor_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.monitor_table.setColumnWidth(1, 210)
        self.ui.monitor_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.ui.monitor_table.setColumnWidth(2, 330)
        self.ui.monitor_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.ui.monitor_table.setColumnWidth(3, 90)
        self.ui.monitor_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.ui.monitor_table.setColumnWidth(4, 170)
        self.ui.monitor_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        # self.ui.monitor_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.load_pages.hlayout4_table.addWidget(self.ui.monitor_table)
        self.ui.monitor_table.verticalHeader().setStyleSheet(f'background-color: {colorx};')

        self.ui.monitor_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.ui.monitor_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 添加CPU使用率
        self.ui.cpu_usage = PyCircularProgress(
            title="处理器占用率",
            value=80,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["text_title"],
            font_size=14,
            bg_color=self.themes["app_color"]["dark_four"]
        )
        self.ui.load_pages.hlayout4_progress.addWidget(self.ui.cpu_usage)
        self.ui.cpu_usage.setFixedSize(160, 160)
        self.ui.usage_spacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.ui.load_pages.hlayout4_progress.addItem(self.ui.usage_spacer)
        self.ui.memory_usage = PyCircularProgress(
            title="内存占用率",
            value=80,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["text_title"],
            font_size=14,
            bg_color=self.themes["app_color"]["dark_four"]
        )
        self.ui.load_pages.hlayout4_progress.addWidget(self.ui.memory_usage)
        self.ui.memory_usage.setFixedSize(160, 160)

        # self.ui.label_progress = QLabel("CPU使用率")
        # self.ui.label_progress.setStyleSheet("font-size: 20px;")
        # self.ui.load_pages.vlayout3_progress.addWidget(self.ui.label_progress)

        # 添加按钮
        self.ui.btn_monitor_load = PyPushButton(
            heigh="40px",
            text="加载文件",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.btn_monitor_start = PyPushButton(
            heigh="40px",
            text="开始检测",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        # self.ui.btn_pause = PyPushButton(
        #     heigh="40px",
        #     text="暂停检测",
        #     radius=8,
        #     color=self.themes["app_color"]["text_foreground"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_hover=self.themes["app_color"]["dark_three"],
        #     bg_color_pressed=self.themes["app_color"]["dark_four"]
        # )
        self.ui.btn_monitor_stop = PyPushButton(
            heigh="40px",
            text="结束检测",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],

        )
        self.ui.btn_monitor_restart = PyPushButton(
            heigh="40px",
            text="重新检测",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.load_pages.glayout4_button.addWidget(self.ui.btn_monitor_load, 0, 0)
        self.ui.load_pages.glayout4_button.addWidget(self.ui.btn_monitor_start, 0, 1)
        # self.ui.load_pages.glayout3_button.addWidget(self.ui.btn_pause, 1, 1)
        self.ui.load_pages.glayout4_button.addWidget(self.ui.btn_monitor_stop, 1, 0)
        self.ui.load_pages.glayout4_button.addWidget(self.ui.btn_monitor_restart, 1, 1)
        # self.ui.btn_pause.setEnabled(False)
        self.ui.btn_monitor_stop.setEnabled(False)
        self.ui.btn_monitor_restart.setEnabled(False)
        self.ui.load_pages.label_run.setStyleSheet("font-size: 25px")

        # PAGE 2
        # CIRCULAR PROGRESS 1
        self.circular_progress_1 = PyCircularProgress(
            value=80,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["text_title"],
            font_size=14,
            bg_color=self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_1.setFixedSize(200, 200)

        # CIRCULAR PROGRESS 2
        self.circular_progress_2 = PyCircularProgress(
            value=45,
            progress_width=4,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["context_color"],
            font_size=14,
            bg_color=self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_2.setFixedSize(160, 160)

        # CIRCULAR PROGRESS 3
        self.circular_progress_3 = PyCircularProgress(
            value=75,
            progress_width=2,
            progress_color=self.themes["app_color"]["pink"],
            text_color=self.themes["app_color"]["white"],
            font_size=14,
            bg_color=self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_3.setFixedSize(140, 140)

        # PY SLIDER 1
        self.vertical_slider_1 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_1.setMinimumHeight(100)

        # PY SLIDER 2
        self.vertical_slider_2 = PySlider(
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_2.setMinimumHeight(100)

        # PY SLIDER 3
        self.vertical_slider_3 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_3.setOrientation(Qt.Horizontal)
        self.vertical_slider_3.setMaximumWidth(200)

        # PY SLIDER 4
        self.vertical_slider_4 = PySlider(
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_4.setOrientation(Qt.Horizontal)
        self.vertical_slider_4.setMaximumWidth(200)

        # ICON BUTTON 1
        self.icon_button_1 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_heart.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Icon button - Heart",
            width=40,
            height=40,
            radius=20,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )

        # ICON BUTTON 2
        self.icon_button_2 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_add_user.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="BTN with tooltip",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )

        # ICON BUTTON 3
        self.icon_button_3 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_add_user.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="BTN actived! (is_actived = True)",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["context_color"],
            is_active=True
        )

        # PUSH BUTTON 1
        self.push_button_1 = PyPushButton(
            text="Button Without Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_1.setMinimumHeight(40)

        # PUSH BUTTON 2
        self.push_button_2 = PyPushButton(
            text="Button With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_2 = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.push_button_2.setMinimumHeight(40)
        self.push_button_2.setIcon(self.icon_2)

        # PY LINE EDIT
        self.line_edit = PyLineEdit(
            text="",
            place_holder_text="Place holder text",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit.setMinimumHeight(30)

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width=50,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )

        # TABLE WIDGETS
        self.table_widget = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("NAME")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("NICK")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("PASS")

        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)

        for x in range(10):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)  # Insert row
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str("Wanderson")))  # Add name
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str("vfx_on_fire_" + str(x))))  # Add nick
            self.pass_text = QTableWidgetItem()
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            self.pass_text.setText("12345" + str(x))
            self.table_widget.setItem(row_number, 2, self.pass_text)  # Add pass
            self.table_widget.setRowHeight(row_number, 22)

        # ADD WIDGETS
        self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_1)
        self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_2)
        self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_3)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_1)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_2)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_3)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_4)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_1)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_2)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_3)
        self.ui.load_pages.row_3_layout.addWidget(self.push_button_1)
        self.ui.load_pages.row_3_layout.addWidget(self.push_button_2)
        self.ui.load_pages.row_3_layout.addWidget(self.toggle_button)
        self.ui.load_pages.row_4_layout.addWidget(self.line_edit)
        self.ui.load_pages.row_5_layout.addWidget(self.table_widget)

        # RIGHT COLUMN

        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)

        # END - EXAMPLE CUSTOM WIDGETS

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized

    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
