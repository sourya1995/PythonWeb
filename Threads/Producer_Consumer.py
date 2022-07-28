import threading

from queue import Queue

def creator(data, q):
    print('creating data and putting it on the queue')
    for item in data:
        evt = threading.Event()
        q.put((item, evt))

        print('waiting for data to be doubled')
        evt.wait()

def my_consumer(q):
    while True:
        data, evt = q.get()
        print('data found to be processed: {}'.format(data))
        processed = data * 2
        print(processed)
        evt.set()
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]
    thread_one = threading.Thread(target=creator, args=(data, q))
    thread_two = threading.Thread(target=my_consumer, args=(q,))
    thread_one.start()
    thread_two.start()
    q.join()