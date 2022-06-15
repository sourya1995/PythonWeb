MAX_SIZE_BYTES=65535
import socket
port = 3000
hostname = '127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, port))
print('Listening at {}'.format(s.getsockname))
while True:
    data, clientAddress = recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    upperCaseMessage = message.upper()
    print('the client at {} says {!r}'.format(clientAddress, message))
    data = upperCaseMessage.encode('ascii')
    s.sendto(clientAddress, data)



