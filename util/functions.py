import collections
import math
import os

import magic

from util.get_file_type import get_file_type


def calculate_entropy(filename, alpha):
    # 读取文件的二进制数据
    with open(filename, 'rb') as f:
        data = f.read()
    if alpha == -1:
        # 计算没有alpha下的信息熵值
        # 计算文件的熵值E
        counter = collections.Counter(data)
        length = len(data)
        file_entropy = sum(-count / length * math.log2(count / length)
                           for count in counter.values())
    else:
        # 将数据分为前40个字节和剩余字节两部分
        head_data = data[:40]
        tail_data = data[40:]
        # 计算前40个字节的熵值Eh
        head_counter = collections.Counter(head_data)
        head_length = len(head_data)
        head_entropy = sum(-count / head_length * math.log2(count / head_length)
                           for count in head_counter.values())
        # 计算剩余字节的熵值Er
        tail_counter = collections.Counter(tail_data)
        tail_length = len(tail_data)
        tail_entropy = sum(-count / tail_length * math.log2(count / tail_length)
                           for count in tail_counter.values())
        # 计算文件信息熵值E
        file_entropy = alpha * head_entropy + (1 - alpha) * tail_entropy
    return file_entropy


def get_file_info(filename):
    if not os.path.exists(filename):
        return None
    try:
        # file_type = magic.from_file(filename, mime=False).split(',')[0]
        # res = magic.from_file(filename, mime=False)
        # file_type = res.split(',')[0] if res else "未知"
        file_type = get_file_type(filename)
        file_size = os.path.getsize(filename)
        return file_type, file_size
    except:
        return None
