import threading
import time
import urllib2

def say_hello():
    print "hello"
if __name__ == '__main__':
     start = time.time()
     threads = []
     threads_count = 10
     print threads_count, "thread(s) running here."
     for i in range(0, threads_count):
         t = threading.Thread(target=say_hello())
         threads.append(t)
     for i in range(0, threads_count):
         threads[i].start()
     for i in range(0, threads_count):
         threads[i].join()
     print "cost time(s):",time.time() - start