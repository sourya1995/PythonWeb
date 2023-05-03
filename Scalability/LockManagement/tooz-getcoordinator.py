import uuid
from tooz import coordination

identifier = str(uuid.uuid4())

c = coordination.get_coordinator("etcd3://localhost", identifier)
c.start(start_heart=True)
c.stop()

print("Done")