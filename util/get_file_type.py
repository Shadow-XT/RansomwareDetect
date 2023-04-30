import mimetypes
import os
import re

import magic


def get_file_type(filename):
    if not os.path.exists(filename):
        return None
    # 判断文件名字是否包含中文
    # if re.search(r"[\u4e00-\u9fa5]", filename):
    # if filename.endswith(".docx"):
    #     # return "Microsoft Word Document"
    #     return mimetypes.guess_type(filename)[0]
    # if not filename.isascii():
    #     with open(filename, "rb") as f:
    #         res = magic.from_buffer(f.read(2048), mime=False)
    # else:
    #     res = magic.from_file(filename, mime=False)
    with open(filename, "rb") as f:
        res = magic.from_buffer(f.read(2048), mime=False)

    return res.split(',')[0] if res else "未知"
