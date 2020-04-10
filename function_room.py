import socket
import ssl
import sys
import timeout_decorator


def validatessl(ip_address, port):
    print("SSL Validation Engine")
    # print(ip_address)
    # print(port)
    raw = ssl.create_default_context()
    plug = raw.wrap_socket(socket.socket(), server_hostname=ip_address)
    plug.connect((ip_address, 443))
    certificate = plug.getpeercert()
    # print(certificate)
    return certificate


def service_name(port, protocol):
    serviceName: str = socket.getservbyport(port, protocol);
    return serviceName


def scanner(target):
    ip_address = target[0]
    port = target[1]

    @timeout_decorator.timeout(1, use_signals=False)
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
                service = service_name(port, 'tcp')
                print(f'Port {port} is open and is running {service}')
                print(port)
                if port == 443:
                    res = validatessl(ip_address, port)
                    print("Website is SSL enabled and expires on ")
                    print(res['notAfter'])
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
        # print("Time Out Error")
