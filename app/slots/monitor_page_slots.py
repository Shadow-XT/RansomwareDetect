import os
import time
from pprint import pprint

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from util.__call_function__ import __call_msgbox__
from util import MonitorThread, get_fileid_by_filename
from util import calculate_entropy


@Slot(QMainWindow)
def btn_monitor_load_slot(win: QMainWindow):
    if win.ui.file_table is None or win.ui.file_table.model().rowCount() <= 0:
        __call_msgbox__("错误", "请先添加文件", win)
        return
    if win.ui.monitor_table is not None and win.ui.monitor_table.model().rowCount() > 0:
        # win.ui.monitor_table.model().removeRows(0, win.ui.monitor_table.model().rowCount())
        # 清空监控列表
        # win.ui.monitor_table.model().removeRows(0, win.ui.monitor_table.model().rowCount())
        win.ui.monitor_table.model().clearRows()
        __call_msgbox__("提示", "监控列表已清空", win)
        return
    win.ui.file_size_to_file = {}
    for index in range(win.ui.file_table.model().rowCount()):
        absfile = win.ui.file_table.model().dataX(index, 0)
        path = os.path.dirname(absfile)
        file = os.path.basename(absfile)
        # id = get_fileid_by_filename(file)
        win.ui.monitor_table.model().appendRow(
            [path, file, "无", os.path.getsize(absfile),
             time.strftime("%Y%m%d %H:%M:%S", time.gmtime(os.path.getmtime(absfile))),
             calculate_entropy(absfile, 0.8)])


@Slot(QMainWindow)
def btn_monitor_start_slot(win: QMainWindow):
    if win.monitor_thread is not None and win.monitor_thread.isRunning():
        __call_msgbox__("错误", "监控检测已经启动", win)
        return
    if win.ui.monitor_table is None or win.ui.monitor_table.model().rowCount() <= 0:
        __call_msgbox__("错误", "请先加载文件", win)
        return
    id_to_file = {}
    files = []
    dirs = set()
    for index in range(win.ui.monitor_table.model().rowCount()):
        file_dir = win.ui.monitor_table.model().dataX(index, 0)
        file_abs = os.path.join(file_dir, win.ui.monitor_table.model().dataX(index, 1)).replace('\\', '/')
        file_id = os.path.getsize(file_abs) // 1024
        # 确保子字典存在
        if file_dir not in id_to_file:
            id_to_file[file_dir] = {}
        id_to_file[file_dir][file_id] = (file_abs, index)
        files.append(file_abs)
        dirs.add(file_dir)
    pprint(files)
    pprint(dirs)
    pprint(id_to_file)

    win.monitor_thread = MonitorThread(dirs, files, id_to_file)
    win.monitor_thread.call_back.connect(monitor_accept)
    win.monitor_thread.start()
    __call_msgbox__("提示", "监控已启动", win)
    win.ui.btn_monitor_stop.setEnabled(True)
    win.ui.btn_monitor_restart.setEnabled(True)
    win.ui.btn_monitor_start.setEnabled(False)

    # win.monitor_thread = MonitorThread(file_to_id)
    # win.monitor_thread.call_back.connect(monitor_accept)
    # win.monitor_thread.start()
    # __call_msgbox__("提示", "监控已启动", win)
    # win.ui.btn_monitor_stop.setEnabled(True)
    # win.ui.btn_monitor_restart.setEnabled(True)
    # win.ui.btn_monitor_start.setEnabled(False)
    # TODO!: 需要完善监控线程

    # win.ui.monitor_thread = MonitorThread()


@Slot(dict)
def monitor_accept(info: dict):
    pass
    # print(f"monitor_accept {os.pathsep}{info['id']}{os.pathsep}{info['file']}"
    #       f"{info['dst_path']}")
    # print(f"monitor accept {info['src'][0]}({info['src'][1]}) -> {info['cur']}")
    # win.ui.monitor_thread.call_back.connect(monitor_accept)
    # win.ui.monitor_thread.start()


@Slot(QMainWindow)
def btn_monitor_stop_slot(win: QMainWindow):
    print(f"btn_monitor_stop {win.objectName()}")
    if win.monitor_thread is not None and win.monitor_thread.isRunning():
        win.monitor_thread.stop()
        win.monitor_thread = None
        __call_msgbox__("提示", "监控检测已停止", win)
        win.ui.btn_monitor_stop.setEnabled(False)
        win.ui.btn_monitor_restart.setEnabled(False)
        win.ui.btn_monitor_start.setEnabled(True)
    else:
        __call_msgbox__("提示", "监控检测未启动", win)


# @Slot(QMainWindow)
# def btn_monitor_pause(win: QMainWindow):
#     print(f"btn_monitor_pause {win.objectName()}")


@Slot(QMainWindow)
def btn_monitor_restart_slot(win: QMainWindow):
    print(f"btn_monitor_restart {win.objectName()}")
    if win.monitor_thread is not None and win.monitor_thread.isRunning():
        win.monitor_thread.stop()
        win.monitor_thread = None
        btn_monitor_start_slot(win)
        __call_msgbox__("提示", "监控检测重启成功", win)
        win.ui.btn_monitor_stop.setEnabled(True)
        win.ui.btn_monitor_restart.setEnabled(True)
        win.ui.btn_monitor_start.setEnabled(False)
    else:
        __call_msgbox__("提示", "监控检测重启失败", win)
