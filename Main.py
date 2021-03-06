#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
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
        qtab.addTab(PreferenceWidget(parent=self), 'Preferences')   # 一番先
        qtab.addTab(ProjectWidget(parent=self), 'Projects')
        qtab.addTab(UnityWidget(parent=self), 'Unity')


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

        self.setWindowIcon(QtGui.QIcon("img\\icon.png"))

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

    ui = MainWindow()

    sys.exit(app.exec_())