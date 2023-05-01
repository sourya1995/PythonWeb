import asyncio

async def add_42(number):
    print("adding 42")
    return 42 + number

async def hello_world():
    print("hello world!")
    result = await add_42(23) #gives control back to event loop - once EL executes add_42(), control is back with hello_world
    return result

event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(hello_world())
    print(result)
finally:
    event_loop.close()