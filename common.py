import inspect
__author__ = 'Yafit'


def print_frame():
    caller_frame_record = inspect.stack()[1]  # 0 represents this line           # 1 represents line at caller
    frame = caller_frame_record[0]
    info = inspect.getframeinfo(frame)
    print info.filename  # __FILE__     -> Test.py
    print info.function  # __FUNCTION__ -> Main
    print info.lineno  # __LINE__     -> 13
