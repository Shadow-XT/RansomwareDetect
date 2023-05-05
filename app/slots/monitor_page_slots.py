import os
import time
from pprint import pprint
import httpx

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from util import MonitorThread, calculate_file_head_hash, calculate_entropy, __call_msgbox__


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
    win.prev_info = {}
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
        win.prev_info[index] = {"currname": file_abs,
                                "file_entropy": calculate_entropy(file_abs, 0.8),
                                "file_head_hash": calculate_file_head_hash(file_abs),
                                "file_size": os.path.getsize(file_abs),
                                "file_mtime": os.path.getmtime(file_abs)}

    win.infected = 0
    win.monitor_thread = MonitorThread(dirs, files, id_to_file)
    win.monitor_thread.call_back.connect(lambda info: monitor_accept(win, info))
    win.monitor_thread.start()
    __call_msgbox__("提示", "监控已启动", win)
    win.ui.btn_monitor_stop.setEnabled(True)
    win.ui.btn_monitor_restart.setEnabled(True)
    win.ui.btn_monitor_start.setEnabled(False)


@Slot(dict)
def monitor_accept(win, info: dict):
    # pprint(f"monitor accept {info['src'][0]}({info['src'][1]}) -> {info['cur']}")

    index = win.ui.monitor_table.model().index(info['src'][1], 2)
    win.ui.monitor_table.model().setData(index, info['cur'])

    file_entropy = calculate_entropy(info['cur'], 0.8)
    file_head_hash = calculate_file_head_hash(info['cur'])

    res = httpx.post(data={
        "src": info['src'][0],
        "curr": info['cur'],
        "pmtime": win.prev[info['src'][1]]["file_mtime"],
        "mtime": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getmtime(info['cur']))),
        "pentropy": win.prev_info[info['src'][1]]["file_entropy"],
        "entropy": file_entropy,
        "pheadHash": win.prev_info[info['src'][1]]["file_head_hash"],
        "headHash": file_head_hash
    })
    # file_size = os.path.getsize(info['cur'])7
    # file_mtime = os.path.getmtime(info['cur'])
    if file_head_hash != win.prev_info[info['src'][1]]["file_head_hash"] and \
            file_entropy > win.prev_info[info['src'][1]]["file_entropy"]:
        win.infected += 1


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
