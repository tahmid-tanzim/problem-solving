from threading import Timer
import time


def heartbeat_tick():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print('im ok ' + current_time)


def heartbeat_tick2():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print('im very good ' + current_time)


class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)


if __name__ == '__main__':

    t1 = RepeatingTimer(20, heartbeat_tick)
    t1.start()  # every 30 seconds, call heartbeat_tick

    t2 = RepeatingTimer(5, heartbeat_tick2)
    t2.start()  # every 30 seconds, call heartbeat_tick

# later
# t.cancel()  # cancels execution