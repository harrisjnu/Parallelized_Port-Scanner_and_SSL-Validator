print ("Multi Process Socket Scanner")


import multiprocessing as mp
from function_room import scanner
import time



print('CPU COUNT AVAILABLE FOR MULTIPROCESSING :  ' + str(mp.cpu_count()))

ip_processed = []
base_ip = 'google.com'
ports = []
range_start = 1
range_end = 1000
for port in range(range_start, range_end):
    ports.append(port)


if __name__ == "__main__":

    targets = list()
    for i in ports:
        item = (base_ip,i)
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

