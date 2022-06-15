MAX_SIZE_BYTES = 65535
import socket
port = 3000
hostname = '127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hosts = []
while True:
    host = input('Enter host address')
    hosts.append((host, port))
    message = input('Enter message to send to server')
    data = message.encode('ascii')
    s.sendto(data, (host, port))
    print('The OS assigned me this address: {}'.format(s.getsockname()))
    data, address = s.recvfrom(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    if(address in hosts):
        print('the server {} replied with {!r}'.format(address, text))
        hosts.remove(address)
    else:
        print('message{!r} from unexpected host {}'.format(text, address))


