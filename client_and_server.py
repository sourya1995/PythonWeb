import argparse, socket
MAX_SIZE_BYTES = 65535

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = '127.0.0.1'
    port = 3000
    s.bind((hostname, port))
    print('listening at {}'.format(s.getsockname()))
    while True:
        data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
        message = data.decode('ascii')
        upperCaseMessage = message.upper()
        print('the client at {} says {!r}'.format(clientAddress, message))
        data = upperCaseMessage.encode('ascii')
        s.sendto(data, clientAddress)

def client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input('input lowercase sentence:')
    data = message.encode('ascii')
    s.sendto('127.0.0.1', 3000)
    print('The OS assigned me this address {}'.format(s.getsockname()))
    data, address = s.recvfrom(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    print('the server {} replied with {!r}'.format(address, text))

if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000, help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)