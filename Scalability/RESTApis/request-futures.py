from concurrent import futures
import requests

with futures.ThreadPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(
            lambda: requests.get("http://example.org")
        )
        for _ in range(8)
    ] #data structure for requests

    results = [
        f.result().status_code 
        for f in futures
    ] #data structure for responses

    print("Results: %s" % results)