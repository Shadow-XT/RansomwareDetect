import json
import os
import re

import httpx
import requests
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow
from qfluentwidgets import InfoBar, InfoBarPosition

from util import __call_msgbox__


@Slot(QMainWindow)
def btn_load_url_slot(win):
    # 判断文件是否存在
    if not os.path.exists("config.json"):
        __call_msgbox__("错误", "配置文件不存在", win)
        return
    # 读取json配置文件
    with open("config.json", "r") as f:
        try:
            profile = json.load(f)
            win.ui.txt_host.setText(profile["api"]["host"])
            win.ui.txt_port.setText(profile["api"]["port"])
        except:
            __call_msgbox__("错误", "配置文件读取失败", win)
            return


@Slot(QMainWindow)
def btn_db_connect_slot(win):
    ip = win.ui.txt_host.text()
    port = win.ui.txt_port.text()
    url = f"http://{ip}:{port}/api/Access"
    ip_regex = re.compile(r'localhost|(^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$)')
    # 端口号正则表达式为0-65535
    port_regex = re.compile(r'^(0|[1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$')
    if not ip_regex.match(ip) or not port_regex.match(port):
        InfoBar.error(
            title='错误',
            content='请输入正确的IP地址和端口号',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,  # won't disappear automatically
            parent=win).show()
        return
    print(url)
    try:
        res = httpx.head(url)
        if res.status_code == 200:
            __call_msgbox__("提示", "连接成功", win)
            win.isConnected = True
            win.url = f'http://{ip}:{port}'
        else:
            __call_msgbox__("错误", "连接失败", win)
        return
    except Exception as e:
        __call_msgbox__("错误", f"连接失败\r\n{e}", win)


@Slot(QMainWindow)
def btn_save_url_slot(win):
    ip = win.ui.txt_host.text()
    port = win.ui.txt_port.text()
    ip_regex = re.compile(r'localhost|(^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$)')
    # 端口号正则表达式为0-65535
    port_regex = re.compile(r'^(0|[1-9]\d{0,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$')
    if not ip_regex.match(ip) or not port_regex.match(port):
        InfoBar.error(
            title='错误',
            content='请输入正确的IP地址和端口号',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,  # won't disappear automatically
            parent=win).show()
        return
    # 将ip和port写入文件
    try:
        with open("config.json", "r") as fr:
            config = json.load(fr)
            # 判断是否存在api节点
            if "api" not in config:
                config["api"] = {}
            config["api"]["host"] = ip
            config["api"]["port"] = port
        with open("config.json", "w") as fw:
            json.dump(config, fw, indent=4)
        __call_msgbox__("提示", "保存成功", win)
    except Exception as e:
        __call_msgbox__("错误", f"保存失败\r\n{e}", win)


@Slot(QMainWindow)
def btn_load_log_slot(win):
    btn_go_to_first(win)


@Slot(QMainWindow)
def btn_go_to_first(win):
    if not win.isConnected:
        __call_msgbox__("错误", "请先连接", win)
        return
    win.ui.pagination.current_page = 1
    try:
        load(win)
    except Exception as e:
        __call_msgbox__("错误", f"加载失败\r\n{e}", win)
        return


@Slot(QMainWindow)
def btn_go_to_previous(win):
    if not win.isConnected:
        __call_msgbox__("错误", "请先连接", win)
        return
    if win.ui.pagination.current_page == 1:
        # win.ui.pagination.update_controls()
        return
    win.ui.pagination.current_page -= 1
    try:
        load(win)
    except Exception as e:
        __call_msgbox__("错误", f"加载失败\r\n{e}", win)
        return


@Slot(QMainWindow)
def btn_go_to_next(win):
    if not win.isConnected:
        __call_msgbox__("错误", "请先连接", win)
        return
    if win.ui.pagination.current_page >= win.ui.pagination.total_pages:
        # win.ui.pagination.update_controls()
        return
    win.ui.pagination.current_page += 1
    try:
        load(win)
    except Exception as e:
        __call_msgbox__("错误", f"加载失败\r\n{e}", win)
        return


@Slot(QMainWindow)
def btn_go_to_last(win):
    if not win.isConnected:
        __call_msgbox__("错误", "请先连接", win)
        return
    if win.ui.pagination.total_pages == 0:
        return
    win.ui.pagination.current_page = win.ui.pagination.total_pages
    try:
        load(win)
    except Exception as e:
        __call_msgbox__("错误", f"加载失败\r\n{e}", win)
        return


@Slot(QMainWindow)
def btn_go_to_jump(win):
    if not win.isConnected:
        __call_msgbox__("错误", "请先连接", win)
        return
    if win.ui.pagination.txt_page.text() == "":
        __call_msgbox__("错误", "请输入页码", win)
        return
    try:
        if win.ui.pagination.total_pages == 0:
            raise Exception("没有数据")
        txt_page = win.ui.pagination.txt_page.text()
        # 判断输入的页码是否合法
        # 判断输入的是否为数字
        if not txt_page.isdigit():
            raise Exception("页码只能是数字")
        page = int(txt_page)
        if page < 1 or page > win.ui.pagination.total_pages:
            raise Exception("页码超出范围")

        win.ui.pagination.current_page = int(page)
        load(win)
    except Exception as e:
        __call_msgbox__("错误", f"{e}", win)
        return


# 加载日志的，分页加载都会调用这个方法
def load(win):
    if not win.isConnected:
        InfoBar.error(
            title='错误',
            content='请先连接数据库',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,  # won't disappear automatically
            parent=win).show()
        return
    url = f"{win.url}/api/Log/GetLogCounts"
    try:
        res = httpx.get(url)
        if res.status_code == 200:
            count = int(res.text)
            mod = count % win.ui.pagination.items_per_page
            div = count // win.ui.pagination.items_per_page
            if mod == 0:
                page = div
            else:
                page = div + 1
            win.ui.pagination.total_items = count
            win.ui.pagination.total_pages = page
            url = f"{win.url}/api/Log/GetLog?page={win.ui.pagination.current_page}" \
                  f"&size={win.ui.pagination.items_per_page}"
            res = requests.get(url)
            if res.status_code == 200:
                if win.ui.database_table.model().rowCount() > 0:
                    win.ui.database_table.model().clearRows()
                datas = res.json()
                for data in datas:
                    win.ui.database_table.model().appendRow(
                        [data["dir"], data["srcName"], data["currName"], data["modifyTime"]])
                InfoBar.success(
                    title='提示',
                    content='日志加载成功',
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=2000,  # won't disappear automatically
                    parent=win).show()
                win.ui.pagination.update_controls()
                win.ui.pagination.page_changed.emit()
                start = (win.ui.pagination.current_page - 1) * win.ui.pagination.items_per_page
                end = min(start + win.ui.pagination.items_per_page, win.ui.pagination.total_items)
                win.ui.database_table.model()._vertical = [i + 1 for i in range(start, end)]
                win.ui.database_table.model().layoutChanged.emit()
    except Exception as e:
        print(e)
        raise e
