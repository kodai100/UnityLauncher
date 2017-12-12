#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import qdarkstyle
from PyQt5.QtWidgets import *
from PreferenceTab import *
from ProjectTab import ProjectWidget
from UnityTab import UnityWidget
from PreferenceTab import PreferenceWidget
from util.Global import Global

class UnityLauncherWidget(QWidget):

    def __init__(self, parent=None):
        super(UnityLauncherWidget, self).__init__(parent)
        self.init()

    def init(self):

        qtab = QTabWidget()
        qtab.addTab(ProjectWidget(parent=self), 'Projects')
        qtab.addTab(UnityWidget(parent=self), 'Unity')
        qtab.addTab(PreferenceWidget(parent=self), 'Preferences')

        hbox = QHBoxLayout()
        hbox.addWidget(qtab)

        self.setLayout(hbox)

        self.show()

        return

class MainWindow(QMainWindow):

    status_bar = None

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setCentralWidget(UnityLauncherWidget())

        self.status_bar = QStatusBar(self)
        Global.setStatusBar(self.status_bar)
        self.setStatusBar(self.status_bar)
        Global.printStatus("Ready", 3000)

        self.setWindowIcon(QIcon("img/icon.png"))

        self.setGeometry(0, 0, 700, 600)
        self.put_center()
        self.setWindowTitle('Unity Launcher')
        self.show()

    def put_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        return


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    app.setWindowIcon(QIcon("img/icon.png"))

    ui = MainWindow()

    sys.exit(app.exec_())