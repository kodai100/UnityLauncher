from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from util.UnityLister import UnityList
import os
from functools import partial

class UnityWidget(QWidget):

    listWidget = None

    def __init__(self, parent=None):
        super(UnityWidget, self).__init__()

        list = UnityList()
        list.show()
        self.listWidget = list

        vbox = QVBoxLayout()
        vbox.addWidget(list)

        buttonGroup = self.button_group()
        vbox.addWidget(buttonGroup)

        self.setLayout(vbox)
        return

    def button_group(self):
        layout = QHBoxLayout()

        runBtn = QPushButton('Run Unity')
        runBtn.setFixedWidth(400)
        runBtn.clicked.connect(self.run_signal)

        launch = QPushButton('Release Notes')
        launch.clicked.connect(self.browse_signal)

        explorer = QPushButton('Explorer')
        explorer.clicked.connect(self.explorer_signal)

        layout.addWidget(runBtn)
        layout.addWidget(launch)
        layout.addWidget(explorer)

        groupBox = QGroupBox()
        groupBox.setLayout(layout)
        groupBox.setStyleSheet("QGroupBox{border:none;}")

        return groupBox

    def explorer_signal(self):
        self.listWidget.explorer()
        return

    def browse_signal(self):
        self.listWidget.browse()
        return

    def run_signal(self):
        self.listWidget.run()
        return