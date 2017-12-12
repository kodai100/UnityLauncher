from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import webbrowser
import re
import os
from sys import platform
from util import FileBrowse

data = [
    ['5.6.0f3', '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['2017.1.0f3', 'C:¥Kodai¥Program Files¥Unity'],
    ['5.6.0f3', 'C:¥Kodai¥Program Files¥Unity'],
    ['5.6.0f3', 'C:¥Kodai¥Program Files¥Unity'],
    ['5.6.0f3', 'C:¥Kodai¥Program Files¥Unity'],
    ['5.6.0f3', 'C:¥Kodai¥Program Files¥Unity'],
    ['5.6.0f3', 'C:¥Kodai¥Program Files¥Unity'],
    ['5.6.0f3', 'C:¥Kodai¥Program Files¥Unity'],
    ['5.6.0f3', 'C:¥Kodai¥Program Files¥Unity']
]


class UnityList(QWidget):

    def __init__(self, parent=None):
        super(UnityList, self).__init__(parent)
        colcnt = len(data[0])
        rowcnt = len(data)
        self.tablewidget = QTableWidget(rowcnt, colcnt)
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablewidget.setStyleSheet("QTableWidget{border:none;}")

        # ヘッダー設定
        horHeaders = ['Version', 'Path']
        self.tablewidget.setHorizontalHeaderLabels(horHeaders)
        header = self.tablewidget.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        # テーブルの中身作成
        for n in range(rowcnt):
            for m in range(colcnt):
                item = QTableWidgetItem(str(data[n][m]))
                self.tablewidget.setItem(n, m, item)

        # レイアウト
        layout = QHBoxLayout()
        layout.addWidget(self.tablewidget)
        self.setLayout(layout)

    def explorer(self):
        file_path = self.tablewidget.item(self.tablewidget.currentRow(), 1).text()
        FileBrowse.explorer(file_path)
        return

    def browse(self):
        version = self.tablewidget.item(self.tablewidget.currentRow(), 0).text()
        FileBrowse.browse(version)
        return