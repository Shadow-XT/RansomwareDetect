import os
from time import sleep

from PySide6.QtCore import QThread, Signal
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from pprint import pprint

from util.fsutil import get_filename_by_fileid


class BaitFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self, call_back, dirs, files, id_to_file, file_to_id):
        super().__init__()
        # self.file_dir_list = file_dir_list
        self._call_back = call_back
        self._dirs = dirs
        self._files = files
        self._id_to_file = id_to_file
        self._file_to_id = file_to_id
        self._infected = []

    def on_modified(self, event):
        if event.is_directory:
            return
        # if "ntuser.dat." in event.src_path:
        #     return
        src_path = event.src_path.replace("\\", "/")
        # 被感染的文件无需再次发射信号
        if src_path in self._infected:
            return

        dirx = os.path.dirname(src_path)
        currfile = None
        try:
            if src_path in self._files:
                idx = self._file_to_id[dirx][src_path][0]
                index = self._file_to_id[dirx][src_path][1]
                for file in os.listdir(dirx):
                    abs_file = f'{dirx}/{file}'
                    if os.path.isfile(abs_file):
                        size = os.path.getsize(abs_file) // 1024
                        if size == idx or size - 1 == idx or size - 2 == idx:
                            currfile = file
                            self._infected.append(abs_file)
                            self._infected.append(currfile)
                            print(f"{idx} modify {src_path} -> {currfile}")
                            self._call_back.emit({"dir": dirx, "src": (src_path, index), "cur": currfile})
                            return
            else:
                size = os.path.getsize(src_path) // 1024
                if size in self._id_to_file[dirx].keys():
                    pass
                elif size - 1 in self._id_to_file[dirx].keys():
                    size -= 1
                elif size - 2 in self._id_to_file[dirx].keys():
                    size -= 2
                else:
                    return
                self._infected.append(src_path)
                currfile = os.path.basename(src_path)
                src_path, index = self._id_to_file[dirx][size]
                self._infected.append(src_path)
                print(f"{size} modify {src_path} -> {currfile}")
                self._call_back.emit({"dir": dirx, "src": (src_path, index), "cur": currfile})
        except FileNotFoundError as e:
            print(e)

    def on_moved(self, event):
        if event.is_directory:
            return
        if event.src_path not in self._files:
            return
        print(f"on moved: {event.src_path}=>{event.dest_path}")


class MonitorThread(QThread):
    call_back = Signal(dict)

    def __init__(self, dirs, files, id_to_file, file_to_id):
        super().__init__()
        self._dirs = dirs
        self._files = files
        self._id_to_file = id_to_file
        self._file_to_id = file_to_id
        self._observer = Observer()
        self._bait_event_handler = BaitFileSystemEventHandler(self.call_back, self._dirs, self._files,
                                                              self._id_to_file, self._file_to_id)
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