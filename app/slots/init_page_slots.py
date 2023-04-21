import json
import os
import winreg

from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from magic import magic

from gui.widgets import PyMessageBoxSingle, PyMessageBoxConfirm


@Slot(QMainWindow)
def btn_load_profile_slot(win: QMainWindow):
    # TODO!: 需要完善配置文件读写
    # 判断配置文件是否存在，不存在就创建
    if os.path.exists("config.json"):
        # 读取json配置文件
        with open("config.json", "r") as f:
            try:
                btn_clear_file_slot(win)
                profile = json.load(f)
                drop_file = []
                for file in profile["bait_file"]:
                    if not os.path.exists(file):
                        drop_file.append(file)
                        continue
                    file_type = magic.from_file(file, mime=True)
                    file_size = os.path.getsize(file)
                    win.ui.file_table.model().appendRow([file, file_type if file_type else "未知", file_size, None])
                if len(drop_file) > 0:
                    __call_msgbox__("错误", f"以下文件不存在，已经被移除:{os.linesep}{os.linesep.join(drop_file)}", win,
                                    12)
            except:
                __call_msgbox__("错误", "配置文件读取失败", win)
                return
    else:
        __call_msgbox__("错误", f"配置文件不存在{os.linesep}请在程序中先手动添加", win)


@Slot(QMainWindow)
def btn_save_profile_slot(win: QMainWindow):
    # TODO!: 需要完善配置文件写
    # 如果没有添加配置文件就不保存
    if win.ui.file_table.model().rowCount() <= 0:
        __call_msgbox__("错误", "请先添加文件", win)
        return
    # 首先通过弹出询问是否需要保存当前的配置
    # 询问是否退出，添加自定义按钮
    msg = PyMessageBoxConfirm(win, "保存配置文件", "你确定要保存当前的配置文件吗？",
                              color=win.themes["app_color"]["dark_four"],
                              selection_color=win.themes["app_color"]["white"],
                              bg_color=win.themes["app_color"]["dark_four"],
                              text_color=win.themes["app_color"]["text_foreground"],
                              btn_color=win.themes["app_color"]["text_foreground"],
                              btn_bg_color=win.themes["app_color"]["dark_one"],
                              btn_bg_color_hover=win.themes["app_color"]["dark_three"],
                              btn_bg_color_pressed=win.themes["app_color"]["dark_four"],
                              buttons={QMessageBox.ButtonRole.YesRole: "确定",
                                       QMessageBox.ButtonRole.NoRole: "取消"},
                              )
    msg.setFont(QFont("微软雅黑", 14))
    msg.exec()
    profile = {"bait_file": []}
    if msg.clickedButton() == msg.btn_dict["确定"]:
        for i in range(win.ui.file_table.model().rowCount()):
            file = win.ui.file_table.model().dataX(i, 0)
            profile["bait_file"].append(file)
        with open("config.json", "w") as f:
            try:
                json.dump(profile, f, indent=4)
                # profile["bait_file"].append(file[0])
                # with open("config.json", "w") as f:
                #     json.dump(profile, f)
            except:
                QMessageBox.critical(win, "错误", "保存配置文件失败")
    elif msg.clickedButton() == msg.btn_dict["取消"]:
        pass
        # print("取消保存配置文件")


@Slot(QMainWindow)
def btn_load_file_slot(win: QMainWindow):
    user_dir = os.path.expanduser('~')
    select_file = QFileDialog.getOpenFileName(
        win, "选择陷阱文件", user_dir, "All Files (*)")[0]
    if select_file == "":
        __call_msgbox__("提示", "未选择文件", win)
        return
    table = win.ui.file_table
    # 添加文件到TableView
    if table:
        # 获取文件的大小
        file_size = os.path.getsize(select_file)
        # 判断设置的文件是不是已经存在与列表中
        for i in range(table.model().rowCount()):
            if table.model().dataX(i, 0) == select_file:
                __call_msgbox__("提示", "文件已存在", win)
                return
        # 获取文件的类型
        file_mime = magic.from_file(select_file, mime=True)
        # if file_mime:
        #     try:
        #         # key_name = f'Software\\Classes\\{file_mime}'
        #         key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, file_mime)
        #         # winreg.SetValue(key, 'FriendlyTypeName', winreg.REG_SZ, '文本文档')
        #         value, _ = winreg.QueryValueEx(key, 'FriendlyTypeName')
        #         file_type = value
        #     except Exception as e:
        #         file_type = "未知文件类型"
        #         print("异常了 ", e, file_mime)
        # else:
        #     file_type = "未知文件类型"
        file_type = magic.from_file(select_file, mime=False)
        table.model().appendRow([select_file, file_type.split(",")[0] if file_type else "未知", file_size, None])
        # table.model().appendRow([select_file, file_size, file_type, None])


@Slot(QMainWindow)
def btn_clear_file_slot(win: QMainWindow):
    # 清除TableView的内容
    if win.ui.file_table:
        for i in range(win.ui.file_table.model().rowCount() - 1, -1, -1):
            win.ui.file_table.model().removeRow(i)


def __call_msgbox__(title, text, win: QMainWindow, font_size=14):
    msg = PyMessageBoxSingle(win, title, text,
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
