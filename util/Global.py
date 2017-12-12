from PyQt5.QtWidgets import *

class Global:

    status_bar = None

    @staticmethod
    def setStatusBar(instance):
        global status_bar
        status_bar = instance
        return

    @staticmethod
    def printStatus(message, sec=None):
        global status_bar
        status_bar.clearMessage()

        if sec is None:
            status_bar.showMessage(message)
        else:
            status_bar.showMessage(message, sec)

        status_bar.show()
        return