from PyQt5.QtWidgets import *

class Global:

    status_bar = None
    unity_parent_path_list = None

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

    @staticmethod
    def set_unity_parent_path_list(list):
        global unity_parent_path_list
        unity_parent_path_list = list

    @staticmethod
    def get_unity_parent_path_list():
        global unity_parent_path_list
        return unity_parent_path_list