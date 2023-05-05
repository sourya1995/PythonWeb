from pymemcache.client import base
import threading

threads = []

def on_visit():
    client = base.Client(('localhost', 11211))
    while True:
        result, cas = client.gets('visitors')
        if result is None:
            result = 1
        else:
            print("Storing:", int(result.decode("utf-8")) + 1)
            result = int(result.decode("utf-8")) + 1
            if client.cas('visitors', result, cas):
                break
            client.cas('visitors', result, cas)

client = base.Client(('localhost', 11211))
client.flush_all()
client.set('visitors', 0)

for _ in range(50):
    t = threading.Thread(target=on_visit)
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('Total visitors: ', client.get('visitors'))