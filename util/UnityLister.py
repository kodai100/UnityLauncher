from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from util import FileBrowse
from util import FileSearch
import subprocess
from util.Global import Global

class UnityList(QWidget):

    def __init__(self, parent=None):
        super(UnityList, self).__init__(parent)

        print('wei', Global.get_unity_parent_path_list())

        self.data = FileSearch.get_unity_version_and_path(Global.get_unity_parent_path_list())    # unity list

        colcnt = 2
        rowcnt = len(self.data)
        self.tablewidget = QTableWidget(rowcnt, colcnt)
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablewidget.setStyleSheet("QTableWidget{border:none;}")

        # ヘッダー設定
        horHeaders = ['Version', 'Path']
        self.tablewidget.setHorizontalHeaderLabels(horHeaders)
        header = self.tablewidget.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        # テーブルの中身作成
        for i, dict in enumerate(self.data):
            item = QTableWidgetItem(dict['version'])
            self.tablewidget.setItem(i, 0, item)
            item = QTableWidgetItem(dict['path'])
            self.tablewidget.setItem(i, 1, item)

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

    def run(self):
        exe_path = self.tablewidget.item(self.tablewidget.currentRow(), 1).text()

        if exe_path is None :
            # alert
            return

        print('Run:', exe_path)
        subprocess.Popen(str(exe_path))
        return