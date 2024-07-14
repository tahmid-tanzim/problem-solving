#!/Library/Frameworks/Python.framework/Versions/3.10/Resources/Python.app/Contents/MacOS/Python

import threading
import time


class TestThreading:
    @staticmethod
    def func(i: int, j: int, sec: int):
        print('Run\n')
        for a in range(i, j):
            print(a, 'Current threads: ', threading.current_thread(), end='\n')
            time.sleep(sec)
        print('Done\n')



