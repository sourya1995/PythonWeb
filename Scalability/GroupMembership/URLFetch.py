import itertools
from tooz import coordination
import uuid
import requests

class URL(str):
    def __tooz__hash(self):
        return self.encode()
    

urls_to_fetch = [URL("https://httpbin.org/bytes/%d" % n) for n in range(100)]

GROUP_NAME = b"fetcher"
MEMBER_ID = str(uuid.uuid4()).encode('ascii')

c = coordination.get_coordinator("etcd3://localhost", MEMBER_ID)
c.start(start_heart=True)

p = c.join_partitioned_group(GROUP_NAME)

try:
    for url in itertools.cycle(urls_to_fetch):
        c.run_watchers()
        if p.belongs_to_self(url):
            try:
                r = requests.get(url)
            except Exception:
                pass
            else:
                print("%s: fetched %s (%d)"
                      % (MEMBER_ID, r.url, r.status_code))
finally:
    c.leave_group(GROUP_NAME).get()

    c.stop()
