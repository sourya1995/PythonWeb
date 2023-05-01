import time

from rq import Queue
from redis import Redis
import requests

q = Queue(name="http", connection=Redis())
job = q.enqueue(requests.get, "http://httpbin.org/delay/1", ttl=60, result_ttl=300)
while job.result is None:
    time.sleep(1)

print(job.result)