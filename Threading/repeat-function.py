from threading import Thread, Event
import time


def heartbeat_tick():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print('im ok ' + current_time)


class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(5):
            print("my thread")
            heartbeat_tick()


if __name__ == '__main__':
    stopFlag = Event()
    thread = MyThread(stopFlag)
    thread.start()
    # this will stop the timer
    stopFlag.set()
