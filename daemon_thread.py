import threading


class DaemonThread(threading.Thread):

    def __init__(self, *args, **kw):
        super(DaemonThread, self).__init__(*args, **kw)
        self.setDaemon(True)
