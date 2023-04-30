# import collections
# import math
# import os
#
# from PySide6.QtCore import QThread, Signal
#
# # class MonitorThread(QThread):
# #     callback = Signal(float)
# #
# #     def run(self):
# #         # 每隔0.5秒获取CPU的值
# #         while not self.isInterruptionRequested():
# #             pass
# #
# #     def stop(self):
# #         self.terminate()
# #         self.wait()
# # 在QThread中使用Watchdog模块实时检测文件的变化
# # 通过信号槽机制将检测到的变化传递给主线程
# # 从而实现实时监测文件的变化
# import collections
# import math
# from PySide6.QtCore import QThread, Signal
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
#
#
# class MonitorThread(QThread):
#     class FileEventHandler(FileSystemEventHandler):
#         def __init__(self):
#             super(MonitorThread.FileEventHandler, self).__init__()
#
#         def on_modified(self, event):
#             pass
#
#     callback = Signal(str)
#
#     def __init__(self, files):
#         super(MonitorThread, self).__init__()
#         self._dirs = set()
#         for file in files:
#             dir = os.path.dirname(file)
#             self._dirs.add(dir)
#         self.observer = Observer()
#         for dir in self._dirs:
#             self.observer.schedule(self.FileEventHandler(), dir, recursive=False)
#             self.observer.start()
#         # self.observer = Observer()
#         # for path in paths:
#         #     self.observer.schedule(self.FileEventHandler(), path, recursive=False)
#         #     self.observer.start()
#
#     def run(self):
#         # 每隔0.5秒获取CPU的值
#         while not self.isInterruptionRequested():
#             self.callback.emit(self.path)
#             self.sleep(0.5)
#
#     def stop(self):
#         self.terminate()
#         self.wait()
import sys
from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def on_modified(self, event):
        self.signal.emit(event.src_path)


class WatchdogThread(QThread):
    file_changed = Signal(str)

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        event_handler = FileChangeHandler(self.file_changed)
        observer = Observer()
        observer.schedule(event_handler, self.path, recursive=True)
        observer.start()
        self.exec()


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("监视文件夹...")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

    def on_file_changed(self, filepath):
        self.label.setText(f"文件已修改: {filepath}")


def main():
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    # 监视文件夹路径
    folder_to_watch = "path/to/folder"
    watchdog_thread = WatchdogThread(folder_to_watch)
    watchdog_thread.file_changed.connect(demo.on_file_changed)
    watchdog_thread.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

import sys
from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def on_modified(self, event):
        self.signal.emit(event.src_path)


class WatchdogThread(QThread):
    file_changed = Signal(str)

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        event_handler = FileChangeHandler(self.file_changed)
        observer = Observer()
        observer.schedule(event_handler, self.path, recursive=True)
        observer.start()
        self.exec()


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("监视文件夹...")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

    def on_file_changed(self, filepath):
        self.label.setText(f"文件已修改: {filepath}")


def main():
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    # 监视文件夹路径
    folder_to_watch = "path/to/folder"
    watchdog_thread = WatchdogThread(folder_to_watch)
    watchdog_thread.file_changed.connect(demo.on_file_changed)
    watchdog_thread.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
