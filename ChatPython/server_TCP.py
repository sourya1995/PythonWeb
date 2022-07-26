import socket
from ssl import SOL_SOCKET

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received %d bytes before socket closed' %(length, len(data)))
        data += more
    return data

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    print('Listening at', sock.getsockname())
    while True:
        print('Waiting for a new connection')
        sc, sockname = sock.accept()
        print('Connection from', sockname)
        print('socket name', sc.getsockname())
        print('socket peer', sc.peername())
        message = recvall(sc, 16)
        print('message from client: ', repr(message))
        sc.sendall(b'Goodbye, client!')
        sc.close()
        print('closing socket')

def client(port):
    host = '127.0.0.1'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned the socket {}'.format(sock.getsockname()))
    sock.sendall(b'Greetings, server')
    reply = recvall(sock, 16)
    print('Server :', repr(reply))
    sock.close()