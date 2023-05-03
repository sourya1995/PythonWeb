import sys
import time
from tooz import coordination

if len(sys.argv) != 3:
    print("Usage: %s <client id> <group id>" % sys.argv[0])
    sys.exit(1)

c = coordination.get_coordinator("etcd3://localhost", sys.argv[1].encode())
c.start(start_heart=True)
group = sys.argv[2].encode()

try:
    c.create_group(group).get()
except coordination.GroupAlreadyExist:
    pass

c.join_group(group, capabilities = {"shirt color": sys.argv[3]}).get()
get_capabilities = [(member, c.get_member_capabilities(group, member)) for member in c.get_members(group).get()]

for member, cap in get_capabilities:
     print("Member %s has capabilities: %s"
          % (member, cap.get()))

members = c.get_members(group)
print(members.get())
time.sleep(60)

c.leave_group(group).get()
c.stop()