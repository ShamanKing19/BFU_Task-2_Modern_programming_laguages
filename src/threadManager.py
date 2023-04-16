import threading
from .thread import WorkerThread


class ThreadManager:
    def __init__(self):
        self.threads = []
        self.lock = threading.Lock()


    def startThread(self, name):
        thread = WorkerThread(name, self.lock)
        thread.start()
        self.threads.append(thread)


    def stopLastThread(self):
        if self.threads:
            lastThread = self.threads.pop()
            lastThread.stop()


    def stopAllThreads(self):
        for thread in self.threads:
            thread.stop()
        self.threads.clear()


    def sendMessage(self, message, target=None):
        if target is None:
            for thread in self.threads:
                thread.addMessageToQueue(message)
            return

        for thread in self.threads:
            if thread.name == target:
                thread.addMessageToQueue(message)
                break
