import os

from PySide6.QtCore import QThread, Signal
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from util.fsutil import get_filename_by_fileid


class BaitFileSystemEventHandler(FileSystemEventHandler):

    def __init__(self, signal, file_to_id, id_to_file):
        super().__init__()
        self.signal = signal
        self.file_to_id = file_to_id
        self.id_to_file = id_to_file
        self.files = list(file_to_id.keys())
        self.ignore_directories = True

    def on_modified(self, event):
        if event.is_directory:
            return
        src_path = os.path.normpath(event.src_path).replace("\\", "/")
        # print(f"modify {src_path}")
        dir = os.path.dirname(src_path)

        # # TODO 等待完成功能
        # if src_path in self.files:
        #     id = self.file_to_id[src_path]
        #     driver = os.path.splitdrive(src_path)[0]
        #     dst_path = get_filename_by_fileid(driver, id)
        #     self.signal.emit({"type": "modify", "id": id, "src_path": src_path, "dst_path": dst_path})
        # print(event.src_path)


class MonitorThread(QThread):
    call_back = Signal(dict)

    def __init__(self, file_to_id, id_to_file):
        super().__init__()
        self._dirs = set()
        for file in file_to_id.keys():
            #  获取文件盘符
            self._dirs.add(os.path.dirname(file))
        self._observer = Observer()
        self._bait_event_handler = BaitFileSystemEventHandler(self.call_back, file_to_id, id_to_file)
        for bait_dir in self._dirs:
            self._observer.schedule(self._bait_event_handler, bait_dir, recursive=False)

    def run(self):
        # 每隔0.5秒获取CPU的值
        if self._observer is not None:
            self._observer.start()
            try:
                while not self.isInterruptionRequested():
                    self.sleep(1)
            except:
                self._observer.stop()
                self._observer = None
            self._observer.join()

    def stop(self):
        if self._observer is not None:
            self._observer.stop()
            self._observer = None
        self.terminate()
        self.wait()

    # 暂停当前线程
    def restart(self):
        # 判断当前线程是不是活动的
        if self.isRunning():
            self.stop()
        if self._observer is not None:
            self._observer.start()
            try:
                while not self.isInterruptionRequested():
                    self.sleep(1)
            except:
                self._observer.stop()
                self._observer = None
            self._observer.join()
