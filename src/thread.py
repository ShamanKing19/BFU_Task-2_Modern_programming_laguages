from threading import Thread, Event
from queue import Queue
import time

class WorkerThread(Thread):
    def __init__(self, name, lock):
        super().__init__(name = name)
        self.stopEvent = Event()
        self.messageQueue = Queue()
        self.lock = lock


    def run(self):
        while not self.stopEvent.is_set():
            if not self.messageQueue.empty():
                message = self.messageQueue.get()
                self.writeToFile(message)
            time.sleep(0.1)


    def stop(self):
        self.stopEvent.set()


    def addMessageToQueue(self, message):
        self.messageQueue.put(message)


    def writeToFile(self, message):
        with self.lock:
            with open(f'./{self.name}.txt', 'a') as f:
                f.write(f'{message}\n')