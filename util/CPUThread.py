from time import sleep

from PySide6.QtCore import Signal, QThread
import psutil


class CPUThread(QThread):
    cpu_value_signal = Signal(tuple)

    def run(self):
        # 每隔0.5秒获取CPU的值
        while not self.isInterruptionRequested():
            cpu_value = psutil.cpu_percent(interval=None)
            # 获取内存占用率
            mem_value = psutil.virtual_memory()
            self.cpu_value_signal.emit((cpu_value, mem_value))
            sleep(1)

    def stop(self):
        self.terminate()
        self.wait()
