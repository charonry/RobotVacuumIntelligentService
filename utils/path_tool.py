"""
系统提供统一的绝对路径
"""

import os

def get_project_root():
    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    return os.path.dirname(current_dir)


def get_abs_path(relative:str)->str:
    return os.path.join(get_project_root(),relative)


if __name__ == '__main__':
    print(get_abs_path("config/config.txt"))
