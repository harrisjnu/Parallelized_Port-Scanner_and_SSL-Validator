
import multiprocessing as mp
from function_room import scanner
import time
from queue import Queue
import threading


print("Multi Process Socket Scanner")


print('CPU COUNT AVAILABLE FOR MULTIPROCESSING :  ' + str(mp.cpu_count()))

print("Please choose execution mode : 1. Multi/Parallel Processing, 2. Multi Threading, 3. Serial Processing")
runtype = input()
runtype = int(runtype)

if runtype == 1:
    runtype = 'parallel'
    print("Initiating Parallel Processing")
elif runtype == 2:
    runtype = 'thread'
    print("Initiating Multi Thread Processing")
elif runtype == 3:
    runtype = 'serial'

print("Code Execution mode is : " + str(runtype))



ip_processed = []
base_ip = 'google.com'
ports = []
range_start = 1
range_end = 1000
for port in range(range_start, range_end):
    ports.append(port)

if __name__ == "__main__":

    if runtype == 'parallel':
        targets = list()
        for i in ports:
            item = (base_ip, i)
            targets.append(item)

        start = time.time()

        processes = list()

        for target in targets:
            processes.append(mp.Process(target=scanner, args=(target,)))

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        end = time.time()
        print('Script execution time:', end - start)


    elif runtype == 'thread':
        print('Threading... ')
        que = Queue()
        def threads():
            while True:
                port = que.get()
                scanner((base_ip,port))
                que.task_done()

        for i in range(50):
            thread = threading.Thread(target=threads)
            thread.daemon = True
            thread.start()

        start = time.time()

        for i in range(1, 1000): # 1000 Ports per go
            que.put(i)

        que.join()

        end = time.time()
        print('Script execution time:', end - start)


    elif runtype == 'serial':
        print("Initiating Serial Processing")
        start = time.time()
        for i in ports:
            scanner((base_ip,i))
        end = time.time()
        print('Script execution time:', end - start)


