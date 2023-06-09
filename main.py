import os
import re
import sys

# 导入设置
from gui.core.json_settings import Settings
# 导入=主窗体
from gui.uis.windows.main_window import *
from gui.uis.windows.main_window.functions_main_window import *
# 导入widgets
from gui.widgets import *
# 导入qt core
from qt_core import *
from util.CPUThread import CPUThread

# 导入slot
from app.slots.init_page_slots import *
from app.slots.monitor_page_slots import *
from app.slots.database_page_slots import *

# 导入配置
# from app.app_init_button import *

#  将QT字体DPI调整为高比例4k显示器
os.environ["QT_FONT_DPI"] = "96"


# 如果是4K显示器启用'os.environ["QT_SCALE_FACTOR"] = "2"'

# 主窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置主窗口
        # 从"gui\uis\main_window\ui_main.py"加载widgets
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # 加载设置
        settings = Settings()
        self.settings = settings.items

        # 设置主窗口
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        self.show()

        self.mousePressed = False
        # 设初始化页面
        self.ui.btn_load_profile.clicked.connect(lambda: btn_load_profile_slot(self))
        self.ui.btn_save_profile.clicked.connect(lambda: btn_save_profile_slot(self))
        self.ui.btn_load_file.clicked.connect(lambda: btn_load_file_slot(self))
        self.ui.btn_clear_file.clicked.connect(lambda: btn_clear_file_slot(self))

        # 数据库页面
        self.ui.btn_load_url.clicked.connect(lambda: btn_load_url_slot(self))
        self.ui.btn_db_connect.clicked.connect(lambda: btn_db_connect_slot(self))
        self.ui.btn_load_log.clicked.connect(lambda: btn_load_log_slot(self))
        self.ui.btn_save_url.clicked.connect(lambda: btn_save_url_slot(self))
        self.ui.pagination.first_button.clicked.connect(lambda: btn_go_to_first(self))
        self.ui.pagination.previous_button.clicked.connect(lambda: btn_go_to_previous(self))
        self.ui.pagination.next_button.clicked.connect(lambda: btn_go_to_next(self))
        self.ui.pagination.last_button.clicked.connect(lambda: btn_go_to_last(self))
        self.ui.pagination.jump_button.clicked.connect(lambda: btn_go_to_jump(self))

        # 设置执行检测页面
        self.ui.btn_monitor_start.clicked.connect(lambda: btn_monitor_start_slot(self))
        self.ui.btn_monitor_stop.clicked.connect(lambda: btn_monitor_stop_slot(self))
        # self.ui.btn_pause.clicked.connect(lambda: btn_monitor_pause(self))
        self.ui.btn_monitor_restart.clicked.connect(lambda: btn_monitor_restart_slot(self))
        self.ui.btn_monitor_load.clicked.connect(lambda: btn_monitor_load_slot(self))

        self.cpu_thread = CPUThread()
        self.cpu_thread.cpu_value_signal.connect(self.set_usage_value)
        self.cpu_thread.start()

        self.monitor_thread = None
        self.isConnected = False
        self.isLoaded = False

    def set_usage_value(self, value):
        self.ui.cpu_usage.set_value(value[0])
        self.ui.memory_usage.set_value(value[1][2])

    # 左边菜单栏被单击时运行
    # 按对象名称/按钮id检查功能
    def btn_clicked(self):
        # 获取被单击的按钮
        btn = SetupMainWindow.setup_btns(self)

        # 如果不是settings按钮则移除左侧菜单栏的选中状态
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # 获取标题栏的settings按钮并将其活动状态设置为false
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)

        # 左侧菜单
        # 主页面按钮
        if btn.objectName() == "btn_home":
            # 选中对应按钮
            self.ui.left_menu.select_only_one(btn.objectName())
            # 加载主页页面
            MainFunctions.set_page(self, self.ui.load_pages.page_1_home)

        # 初始化页面按钮
        if btn.objectName() == "btn_init":
            self.ui.left_menu.select_only_one(btn.objectName())
            # 加载初始化页面
            MainFunctions.set_page(self, self.ui.load_pages.page_2_init_file)

        # TODO: 需要完成数据库页面的功能
        if btn.objectName() == "btn_database":
            self.ui.left_menu.select_only_one(btn.objectName())
            # 加载数据库界面
            MainFunctions.set_page(self, self.ui.load_pages.page_3_database)

        # 执行检测按钮
        if btn.objectName() == "btn_run":
            self.ui.left_menu.select_only_one(btn.objectName())
            # 加载执行检测页面
            MainFunctions.set_page(self, self.ui.load_pages.page_4_monitor)

        # 部件页面按钮
        if btn.objectName() == "btn_widgets":
            self.ui.left_menu.select_only_one(btn.objectName())
            # 加载部件页面
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # # LOAD USER PAGE
        # if btn.objectName() == "btn_add_user":
        #     self.ui.left_menu.select_only_one(btn.objectName())
        #     # Load Page 3
        #     MainFunctions.set_page(self, self.ui.load_pages.page_3)

        # 信息按钮
        if btn.objectName() == "btn_info":
            # 如果左侧栏当前不可见，则显示左侧栏并选择“btn_info”标签页
            if not MainFunctions.left_column_is_visible(self):
                # 1. 将btn_info标签页设置为选中状态
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                # 2. 显示/隐藏左侧栏
                MainFunctions.toggle_left_column(self)
                # 3. 再次将btn_info标签页设置为选中状态
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            # 如果左侧栏可见，则检查是否单击了“btn_close_left_column”按钮
            else:
                # 如果单击了“btn_close_left_column”按钮
                if btn.objectName() == "btn_close_left_column":
                    # 1. 取消选择所有标签页
                    self.ui.left_menu.deselect_all_tab()
                    # 2. 显示/隐藏左侧栏
                    MainFunctions.toggle_left_column(self)
                # 如果没有单击“btn_close_left_column”按钮,将“btn_info”标签页设置为选中状态
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # 不管左侧栏是否可见，都将左侧栏菜单更改为“menu_2”
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Info tab",
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )

        # 设置按钮，同上
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

        # 标题栏菜单
        # 标题栏中的settings按钮
        if btn.objectName() == "btn_top_settings":
            # 如果右侧菜单栏不可见，则将按钮设置为活动状态
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)
                # 显示右侧菜单栏
                MainFunctions.toggle_right_column(self)
            # 如果右侧菜单栏可见，则将按钮设置为非活动状态
            else:
                btn.set_active(False)
                # 隐藏右侧菜单栏
                MainFunctions.toggle_right_column(self)
            # 获取左侧菜单栏中的“设置”按钮，并将其活动选项卡的状态设置为“False”。
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)

            # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # 当左侧的按钮被松开时运行函数
    # 按对象的名称或者按钮id检查功能
    def btn_released(self):
        # 获取按钮点击
        btn = SetupMainWindow.setup_btns(self)
        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # 窗口大小调整事件
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    def mousePressEvent(self, event):
        if not event.button() == Qt.LeftButton:
            return
        if event.button() == Qt.LeftButton:
            self.mousePressed = True
            self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.mousePressed:
            newPos = event.globalPosition().toPoint()
            diff = newPos - self.dragPos
            self.move(self.pos() + diff)
            self.dragPos = newPos

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePressed = False
            self.dragPos = QPoint(0, 0)

    # 设置关闭事件
    def closeEvent(self, event):
        # 询问是否退出，添加自定义按钮
        msg = PyMessageBoxConfirm(self, "退出程序", "你确定要退出程序吗？",
                                  color=self.themes["app_color"]["dark_four"],
                                  selection_color=self.themes["app_color"]["white"],
                                  bg_color=self.themes["app_color"]["dark_four"],
                                  text_color=self.themes["app_color"]["text_foreground"],
                                  btn_color=self.themes["app_color"]["text_foreground"],
                                  btn_bg_color=self.themes["app_color"]["dark_one"],
                                  btn_bg_color_hover=self.themes["app_color"]["dark_three"],
                                  btn_bg_color_pressed=self.themes["app_color"]["dark_four"],
                                  buttons={QMessageBox.ButtonRole.YesRole: "确定",
                                           QMessageBox.ButtonRole.NoRole: "取消"})
        msg.setFont(QFont("微软雅黑", 18))
        msg.exec()
        if msg.clickedButton() == msg.btn_dict["确定"]:
            if self.cpu_thread and self.cpu_thread.isRunning():
                self.cpu_thread.stop()
            if self.monitor_thread and self.monitor_thread.isRunning():
                self.monitor_thread.stop()
            event.accept()
        elif msg.clickedButton() == msg.btn_dict["取消"]:
            event.ignore()


# 应用程序开始运行
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
