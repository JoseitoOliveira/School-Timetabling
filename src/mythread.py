from PyQt5.QtCore import QObject, QThread
import time


class MyThread(QThread):
    def run(self):
        self.exec_()


class Worker(QObject):

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.running = True

    def stop(self):
        self.running = False


class CCWorker(Worker):

    def __init__(self, name, time_sleep, check_connection, disconnect, parent=None) -> None:
        super().__init__(parent=parent)
        self.func_check_connection = check_connection
        self.func_disconnect = disconnect
        self.name = name
        self.time_sleep = time_sleep

    def run(self):
        while connected := self.func_check_connection():
            time.sleep(self.time_sleep)

        self.func_disconnect()
        print(f'{self.name} Finalizada')
