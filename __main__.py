print ("Multi Process Socket Scanner")

import socket
import sys
import timeout_decorator



ip_address = "10.10.0.1"
port = 443
target = (ip_address,port)




def scanner(target):
    ip_address = target[0]
    port = target[1]
    @timeout_decorator.timeout(2, use_signals=False)
    def timelimiter():
        try:
            plug = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # AF_INET: IPv4, AF_INET6: IPv6, SOCK.STREAM:TCP, SOCK.DGRAM: UDP
            socket.setdefaulttimeout(1)
            print("Set Timeout")
            try:
                print("Trying Response")
                response = plug.connect_ex((ip_address,port))
                print("Tried response")
                plug.close()
            except:
                pass
            if response == 0:
                print ('Port is open')
            else:
                print(response)
                print(type(response))
                pass
        except TimeoutError:
            print("Time Out Error")
        except:
            print("Encountered some error")
            sys.exit()

    try:
        timelimiter()

    except timeout_decorator.timeout_decorator.TimeoutError:
        print("Time Out Error")

scanner(target)
