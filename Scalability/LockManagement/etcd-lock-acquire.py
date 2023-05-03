import etcd3

def lock_acquire(lock):
    lock.acquire()

    try:
        print("do something")
    finally:
        lock.release()


def lock_with(lock):
    with lock:
        print("do something else")

client = etcd3.client()
lock = client.lock("foobar")
lock_acquire(lock)
lock_with(lock)
