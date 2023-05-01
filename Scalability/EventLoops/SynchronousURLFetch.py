import requests, time

urls = ["u1", "u2", "u3"]

start_time = time.time()
for URL in urls:
    r = requests.get(url=URL)
    data = r.content
    print(data)

print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))