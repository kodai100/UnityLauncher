from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from util.ProjectLister import ProjectList
import os
from functools import partial

class ProjectWidget(QWidget):

    listWidget = None

    def __init__(self, parent=None):
        super(ProjectWidget, self).__init__()

        list = ProjectList()
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

        launch = QPushButton('Launch')
        launch.setFixedWidth(400)

        downloadBtn = QPushButton('Download')
        downloadBtn.clicked.connect(self.download_signal)

        explorer = QPushButton('Explorer')
        explorer.clicked.connect(self.explorer_signal)

        layout.addWidget(launch)
        layout.addWidget(downloadBtn)
        layout.addWidget(explorer)

        groupBox = QGroupBox()
        groupBox.setLayout(layout)
        groupBox.setStyleSheet("QGroupBox{border:none;}")

        return groupBox

    def download_signal(self):
        self.listWidget.browse()
        return

    def explorer_signal(self):
        self.listWidget.explorer()
        return