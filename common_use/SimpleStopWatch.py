import time

print('Press enter to begin, Press Ctrl + C to stop')
while True:
    try:
        text = input()
        startTime = time.time()
        print('Started')
        while True:
            print('Time Elapsed: ', round(time.time()-startTime), 'secs', end="\n")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped")
        endTime = time.time()
        print('Total Time: ', round(endTime - startTime, 2), 'secs')
        break


