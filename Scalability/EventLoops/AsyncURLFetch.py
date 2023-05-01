import aiohttp, asyncio, time

urls = ["u1", "u2", "u3"]

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response
        
loop = asyncio.get_event_loop()
coroutines = []

for URL in urls:
    coroutines.append(get(URL))


start_time = time.time()
results = loop.run_until_complete(asyncio.gather(*coroutines))
print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))

print("Results: %s" % results)