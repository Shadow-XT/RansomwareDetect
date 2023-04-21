from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow


@Slot(QMainWindow)
def btn_monitor_start(win: QMainWindow):
    print(f"btn_monitor_start {win.objectName()}")


@Slot(QMainWindow)
def btn_monitor_stop(win: QMainWindow):
    print(f"btn_monitor_stop {win.objectName()}")


@Slot(QMainWindow)
def btn_monitor_pause(win: QMainWindow):
    print(f"btn_monitor_pause {win.objectName()}")


@Slot(QMainWindow)
def btn_monitor_restart(win: QMainWindow):
    print(f"btn_monitor_restart {win.objectName()}")
