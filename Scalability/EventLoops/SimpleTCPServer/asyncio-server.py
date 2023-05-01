import asyncio
from asyncio import transports



SERVER_ADDRESS = ('0.0.0.0', 1234)

class YellEchoServer(asyncio.Protocol):
    def connection_made(self, transport): #underlying socket and transport
        self.transport = transport
        print("Connection received from:", transport.get_extra_info('peername'))

    def data_received(self, data): #called each time data is received
        self.transport.write(data.upper())

    def connection_lost(self, exc):
        print("Connection lost")

event_loop = asyncio.get_event_loop()

factory = event_loop.create_server(YellEchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)

try:
    event_loop.run_forever()
    print("Server started")
finally:
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    event_loop.close()