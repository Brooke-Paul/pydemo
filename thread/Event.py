from threading import Thread, Event
import time


# code to execute in an independent thread
def countdown(n, start_event):
    print("countdown starting")
    start_event.set()
    while n > 0:
        print("T-times", n)
        n -= 1
        time.sleep(1)


# create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print("Launching countdown")
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# wait for the thread to start
started_evt.wait()
print("countdown is running")

