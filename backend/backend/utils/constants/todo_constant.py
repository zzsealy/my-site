from enum import Enum

class TagConstant(Enum):
    """
    0:周目标 1:月目标 2:短期目标 3:长期目标'
    """
    WEEK = 0
    MONTH = 1
    SHORT = 2
    LONG = 3

class StatusConstant(Enum):
    """
    0: 进行中
    1: 完成
    """
    PROCESS = 0
    FINISH = 1
