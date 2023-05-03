import sys
import time
from tooz import coordination

if len(sys.argv) != 3:
    print("Usage: %s <client id> <group id>" % sys.argv[0])
    sys.exit(1)

c = coordination.get_coordinator(
    "etcd3://localhost",
    sys.argv[1].encode())

c.start(start_heart=True)

group = sys.argv[2].encode()

p = c.join_partitioned_group(group)

try:
    while True:
        print(p.members_for_object("foobar"))
        time.sleep(1)
finally:
    c.leave_group(group).get()
    c.stop()