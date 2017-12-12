from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from util import FileBrowse

data = [
    ['WaveSimulation', '2017.1.2f0', '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher'],
    ['WaveSimulation', '2017.1.2f0',
     '/Users/Kodai/Documents/PythonVirtualEnvs/Python3/UnityLauncher/projects/UnityLauncher']
]


class ProjectList(QWidget):

    def __init__(self, parent=None):
        super(ProjectList, self).__init__(parent)
        colcnt = len(data[0])
        rowcnt = len(data)
        self.tablewidget = QTableWidget(rowcnt, colcnt)
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablewidget.setStyleSheet("QTableWidget{border:none;}")

        #ヘッダー設定
        horHeaders = ['Name','Version','Path']
        self.tablewidget.setHorizontalHeaderLabels(horHeaders)
        header = self.tablewidget.horizontalHeader()
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        #テーブルの中身作成
        for n in range(rowcnt):
            for m in range(colcnt):
                item = QTableWidgetItem(str(data[n][m]))
                self.tablewidget.setItem(n, m, item)

        #レイアウト
        layout = QHBoxLayout()
        layout.addWidget(self.tablewidget)
        self.setLayout(layout)

    def explorer(self):
        file_path = self.tablewidget.item(self.tablewidget.currentRow(), 2).text()
        FileBrowse.explorer(file_path)
        return

    def browse(self):
        version = self.tablewidget.item(self.tablewidget.currentRow(), 1).text()
        FileBrowse.browse(version)
        return