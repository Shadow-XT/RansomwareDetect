import os
import subprocess
import string


def get_fileid_by_filename(filename: str) -> str:  # 通过文件名查看文件id
    if os.path.exists(filename):  # 文件存在则执行cmd命令取出回显结果
        return os.popen(f'fsutil file queryfileid "{filename}"').read().split(' ')[-1].strip()
    else:  # 文件不存在报错
        raise FileNotFoundError


def get_filename_by_fileid(driver: str, fileid: str):  # 通过文件id查看文件
    if os.path.exists(driver):  # 文件驱动器存在
        with os.popen(f'fsutil file queryFileNameById {driver} {fileid}') as fp:
            bf = fp.buffer.read()  # 读取执行cmd命令后的缓冲区
            try:  # 默认是utf8，出错则调用gbk解码，获取文件绝对路径
                filepath = bf.decode().split('?\\')[-1].strip()
            except:
                filepath = bf.decode('gbk').split('?\\')[-1].strip()
        # filepath = os.popen(f'fsutil file queryFileNameById {driver} {fileid}',encoding='utf-8').read().split('?\\')[
        #     -1].strip()
        return filepath.replace('\\', '/')  # 返回文件绝对路径
    else:
        raise FileNotFoundError
