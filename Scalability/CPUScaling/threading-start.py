import threading

def print_something(something):
    print(something)

t = threading.Thread(target=print_something, args="hello")
t.daemon = True #background thread
t.start()
print("thread started")
