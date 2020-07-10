import time
for i in range(5):
    t0= time.time()
    print(time.time())
    time.sleep(1)
    t1 = time.time() - t0
    print("Time elapsed: ", t1)


'''# Python program showing
# how to kill threads
# using set/reset stop
# flag

import threading
import time


def run():
    while True:
        print('thread running')
        global stop_threads
        if stop_threads:
            print("stop")
            break


stop_threads = False
t1 = threading.Thread(target=run)
t1.start()
time.sleep(1)
stop_threads = True
t1.join()
time.sleep(1)
stop_threads = False
t1.join()
print('thread killed')'''