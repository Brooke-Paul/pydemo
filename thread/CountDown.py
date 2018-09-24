import time
import threading
from threading import Thread


# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


def countdown(n):
    while n > 0:
        print("this is", n)
        n -= 1
        time.sleep(1)

    print('thread %s is end...' % threading.current_thread().name)

t = Thread(target=countdown, args=(10, ))
t.start()

