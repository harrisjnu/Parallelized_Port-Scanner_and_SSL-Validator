import socket
import sys
import timeout_decorator


def service_name(port,protocol):
    serviceName = socket.getservbyport(port,protocol);
    return serviceName

def scanner(target):
    ip_address = target[0]
    port = target[1]

    @timeout_decorator.timeout(2, use_signals=False)
    def timelimiter():
        try:
            plug = socket.socket(socket.AF_INET,
                                 socket.SOCK_STREAM)  # AF_INET: IPv4, AF_INET6: IPv6, SOCK.STREAM:TCP, SOCK.DGRAM: UDP
            socket.setdefaulttimeout(1)
            try:
                response = plug.connect_ex((ip_address, port))
                plug.close()
            except:
                pass
            if response == 0:
                service = service_name(port,'tcp')
                print(f'Port {port} is open and is running {service}')
            else:
                pass
        except TimeoutError:
            print("Time Out Error")
        except:
            print("Encountered some error")
            sys.exit()

    try:
        timelimiter()

    except timeout_decorator.timeout_decorator.TimeoutError:
        pass
        #print("Time Out Error")
