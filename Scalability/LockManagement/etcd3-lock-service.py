import threading
import time
import cotyledon
import etcd3

class PrinterService(cotyledon.Service):
    name="printer"

    def __init__(self, worker_id):
        super(PrinterService, self).__init__(worker_id)
        self._shutdown = threading.Event()
        self.client = etcd3.client()

    def run(self):
        while not self._shutdown_is_set():
            with self.client.lock("print"):
                print("printing" % self.worker_id)
                time.sleep(1)

    def terminate(self):
        self._shutdown.set()


manager = cotyledon.ServiceManager()
manager.add(PrinterService, 4)
manager.run()
