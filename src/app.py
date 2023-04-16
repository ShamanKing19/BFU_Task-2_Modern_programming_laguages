import tkinter as tk
from tkinter import simpledialog, Button, Listbox, Tk
from .threadManager import ThreadManager

class App:
    width = 400
    height = 400


    def __init__(self):
        self.threadManager = ThreadManager()
        self.window = self.createWindow()
        
        Button(self.window, text="Start", command=self.onStart).pack()
        Button(self.window, text="Stop", command=self.onStop).pack()
        Button(self.window, text="Send", command=self.onSend).pack()
        Button(self.window, text="Exit", command=self.onExit).pack()
        self.threadListbox = Listbox(self.window)
        self.threadListbox.pack()

        self.window.mainloop()


    def createWindow(self):
        window = Tk()
        window.geometry(f'{self.width}x{self.height}')
        window.title("Менеджер потоков")
        return window


    def onStart(self):
        threadName = f'thread-{len(self.threadManager.threads)}'
        self.threadManager.startThread(threadName)
        self.updateThreadList()


    def onStop(self):
        self.threadManager.stopLastThread()
        self.updateThreadList()


    def onExit(self):
        self.threadManager.stopAllThreads()
        self.window.quit()


    def onSend(self):
        target = None
        targets = [thread.name for thread in self.threadManager.threads]
        if targets:
            target = simpledialog.askstring(
                "Поток", "Введите название потока, либо оставьте поле пустым, чтобы отправить сообщение всем:", parent=self.window)
            if target not in targets and target is not None:
                return
        message = simpledialog.askstring(
            "Сообщение", "Введите сообщение:", parent=self.window)
        if message:
            self.threadManager.sendMessage(message, target)


    def updateThreadList(self):
        self.threadListbox.delete(0, tk.END)
        for thread in self.threadManager.threads:
            self.threadListbox.insert(tk.END, f'{thread.name}')

