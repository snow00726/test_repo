import os
from typing import List, Tuple, Dict, Set, Union, Any

from scan import Scan


def all_files(dirname):
    result = []  # 所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            if not filename.endswith('.py'):
                continue
            apath = os.path.join(maindir, filename)   # 合并成一个完整路径
            result.append(apath)
    return result
