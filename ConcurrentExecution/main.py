#!/Library/Frameworks/Python.framework/Versions/3.10/Resources/Python.app/Contents/MacOS/Python

import threading
from TestThreading import TestThreading


if __name__ == "__main__":
    x = threading.Thread(target=TestThreading.func, args=(10, 15, 2,))
    x.start()
    y = threading.Thread(target=TestThreading.func, args=(1, 9, 1,))
    y.start()
    print('Active threads: ', threading.active_count(), end='\n')
    print('Current threads: ', threading.current_thread(), end='\n')




