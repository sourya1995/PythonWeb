import asyncio
from asyncio import transports

SERVER_ADDRESS = ('0.0.0.0', 1234)

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def talk(self):
        self.transport.write(self.message)

    def connection_made(self, transport):
        self.transport = transport
        self.talk()

    def data_received(self, data):
        self.talk()

    def connection_lost(self, exc):
        self.loop.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(loop.create_connection(
    lambda: EchoClientProtocol(b'Hello World!', loop),
    *SERVER_ADDRESS))
try:
    loop.run_forever()

finally:
    loop.close()