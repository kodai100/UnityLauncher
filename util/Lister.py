from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class List(QListWidget):

    def __init__(self, parent=None):
        super(List, self).__init__(parent)

    def addRow(self, path):
        self.addItem(path)
        return

    def removeSelectedRow(self):
        listItems = self.selectedItems()

        if not listItems:
            return

        # for multiple selection
        for item in listItems:
            self.takeItem(self.row(item))

        return
