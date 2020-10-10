import urllib.request as request
import time
import _thread


ts = time.time()
req = request.urlopen('http://www.yiibai.com')
pageHtml = req.read()
te = time.time()
print("Page Fetching Time : {} Seconds".format(te-ts))


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s : %s" % (thread_name, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time("thread-1", 2))
    _thread.start_new_thread(print_time("thread-2", 4))

except:
    print("Error: unable to start thread")
while 1:
    pass


