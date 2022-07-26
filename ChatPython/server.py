import socket

MAX_SIZE_BYTES=65535
port=3000
hostname='127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, port))
print('Listening on {}'.format(s.getsockname()))
while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    print('the client at {} says {!r}'.format(clientAddress, message))
    msg_to_send = input('what do you wanna send?')
    data = msg_to_send.encode('ascii')
    s.sendto(data, clientAddress)
