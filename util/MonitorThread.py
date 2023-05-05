import os

from PySide6.QtCore import QThread, Signal
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from pprint import pprint

from util.fsutil import get_filename_by_fileid


class BaitFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self, call_back, dirs, files, id_to_file):
        super().__init__()
        # self.file_dir_list = file_dir_list
        self._call_back = call_back
        self._dirs = dirs
        self._files = files
        self._id_to_file = id_to_file

        # dirx = os.path.join(os.path.expanduser("~"), ".afiles")
        # file_with_dir = [os.path.join(dirx, file) for file in os.listdir(dirx)]
        # self.files = [file.replace("\\", "/") for file in file_with_dir if os.path.isfile(file)]
        # self.size_to_file = {}
        # for file in self.files:
        #     self.size_to_file[os.path.getsize(file) // 1024] = file
        # 将上面循环改为一行代码
        # self.size_to_file = {os.path.getsize(file) // 1024: file for file in self.files}
        # print(self.size_to_file)
        # self.file_size = list(self.size_to_file.keys())
        # print(self.file_size)
        # 被感染的文件
        self._infected = []
        pprint(self._files)

    def on_modified(self, event):
        if event.is_directory:
            return
        src_path = event.src_path.replace("\\", "/")
        # 被感染的文件无需再次发射信号
        if src_path in self._infected:
            return
        if src_path in self._files:
            return

        try:
            size = os.path.getsize(src_path) // 1024
            dirx = os.path.dirname(src_path)
            if dirx not in self._dirs:
                return
            if size in self._id_to_file[dirx].keys():
                pass
            elif (size - 1) in self._id_to_file[dirx].keys():
                size -= 1
            else:
                return
            # pprint(f"{size} modify {self._id_to_file[dirx][size]} -> {src_path}")
            self._infected.append(src_path)
            self._call_back.emit({"src": self._id_to_file[dirx][size], "cur": os.path.basename(src_path)})
        except FileNotFoundError:
            pass
            # pprint(f"file not found {src_path}")


class MonitorThread(QThread):
    call_back = Signal(dict)

    def __init__(self, dirs, files, id_to_file):
        super().__init__()
        self._dirs = dirs
        self._files = files
        self._id_to_file = id_to_file
        # self._dirs = set()
        # for file in file_to_id.keys():
        #     #  获取文件盘符
        #     self._dirs.add(os.path.dirname(file))
        self._observer = Observer()
        self._bait_event_handler = BaitFileSystemEventHandler(self.call_back, self._dirs, self._files, self._id_to_file)
        for bait_dir in self._dirs:
            self._observer.schedule(self._bait_event_handler, bait_dir, recursive=False)

    def run(self):
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

    # def __init__(self, signal, file_to_id, id_to_file):
    #     super().__init__()
    #     self.signal = signal
    #     self.file_to_id = file_to_id
    #     self.id_to_file = id_to_file
    #     self.files = list(file_to_id.keys())
    #     self.ignore_directories = True
    #
    # def on_modified(self, event):
    #     if event.is_directory:
    #         return
    #     src_path = os.path.normpath(event.src_path).replace("\\", "/")
    #     # print(f"modify {src_path}")
    #     dir = os.path.dirname(src_path)
    #
    #     # # TODO 等待完成功能
    #     # if src_path in self.files:
    #     #     id = self.file_to_id[src_path]
    #     #     driver = os.path.splitdrive(src_path)[0]
    #     #     dst_path = get_filename_by_fileid(driver, id)
    #     #     self.signal.emit({"type": "modify", "id": id, "src_path": src_path, "dst_path": dst_path})
    #     # print(event.src_path)
