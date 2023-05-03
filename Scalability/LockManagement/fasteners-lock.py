import time
import fasteners

lock = fasteners.InterProcessLock("/tmp/myLock")
with lock:
    print("Access Locked")
    time.sleep(1)