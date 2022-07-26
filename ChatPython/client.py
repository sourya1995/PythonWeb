MAX_SIZE_BYTES = 65535
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostname = '127.0.0.1'
port=3000
while True:
    s.connect((hostname, port))
    message = input('Input message to the server: ')
    data = message.encode('ascii')
    s.send(data)
    data = s.recv(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    print('the server {} responded with {!r}'.format(text))