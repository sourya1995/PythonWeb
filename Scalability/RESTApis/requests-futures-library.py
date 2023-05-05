from requests_futures import sessions
session = sessions.FuturesSession() #2 workers by default

futures = [
    session.get("http://example.org")
    for _ in range(8)
]

results = [
    f.result().status_code
    for f in futures
]

print("Results: %s" % results)