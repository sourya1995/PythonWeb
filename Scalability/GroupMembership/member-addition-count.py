import sys
import time
from tooz import coordination

members = 1
def addMemberCount(group):
    global members
    print("Adding member")
    members += 1
    print("Total members now: ", members)

def subMemberCount(group):
    global members
    print("removing members")
    members -= 1
    print("Total members now: ", members )

if len(sys.argv) != 3:
    print("Usage: %s <client id> <group id>" % sys.argv[0])
    sys.exit(1)

c = coordination.get_coordinator("etcd3://localhost/?timeout=3", sys.argv[1].encode())
c.start(start_heart=True)
group = sys.argv[2].encode()

try:
    c.create_group(group).get()
except coordination.GroupAlreadyExist:
    pass

c.join_group(group).get()
c.watch_join_group(group, addMemberCount)
c.watch_leave_group(group, subMemberCount)

while True:
    c.run_watchers()
    time.sleep(1)

c.leave_group(group).get()

c.stop()
