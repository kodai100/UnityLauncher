from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from util.Lister import List
import os
from functools import partial
import json
import collections
from util.Global import Global

class PreferenceWidget(QWidget):

    list_holder = []

    def __init__(self, parent=None):
        super(PreferenceWidget, self).__init__()

        vbox = QVBoxLayout()

        list1 = self.list_group("Project Search Dir")

        list2 = self.list_group("Unity Search Dir")

        hbox = QHBoxLayout()
        saveBtn = QPushButton('Save')
        saveBtn.clicked.connect(partial(self.save_signal, list1, list2))
        saveBtn.setStyleSheet("QPushButton{background-color:#555;}")
        refleshBtn = QPushButton('Reflesh')
        refleshBtn.clicked.connect(self.reflesh_signal)
        hbox.addWidget(saveBtn)
        hbox.addWidget(refleshBtn)
        groupBox = QGroupBox()
        groupBox.setLayout(hbox)
        groupBox.setStyleSheet("QGroupBox{border:none;}")

        vbox.addWidget(list1)
        vbox.addWidget(list2)
        vbox.addWidget(groupBox)

        self.init_list()

        self.setLayout(vbox)


        return

    def init_list(self):
        readData = self.readSavedData()
        print('Read:', readData)

        for i in range(len(readData)):
            for data in readData[i]:
                self.list_holder[i].addItem(data)

        Global.set_unity_parent_path_list(readData[1])

        print(self.list_holder[0].item)

    def list_group(self, name):

        layout = QVBoxLayout()

        list = List()
        list.show()
        layout.addWidget(list)
        self.list_holder.append(list)

        buttonGroup = self.button_group(list)
        layout.addWidget(buttonGroup)

        groupBox = QGroupBox(name)
        groupBox.setLayout(layout)
        return groupBox

    def button_group(self, lister):
        layout = QHBoxLayout()

        addBtn = QPushButton('Add Parent Directory')
        addBtn.clicked.connect(partial(self.add_signal, lister))

        removeBtn = QPushButton('Remove')
        removeBtn.clicked.connect(partial(self.remove_signal, lister))

        layout.addWidget(addBtn)
        layout.addWidget(removeBtn)

        groupBox = QGroupBox()
        groupBox.setLayout(layout)

        groupBox.setStyleSheet("QGroupBox{border:none;}")

        return groupBox

    def readSavedData(self):

        fr = open('data/data.json', 'r')
        list = json.load(fr)
        print(list)

        return [list["ProjectDir"]["path"], list["UnityDir"]["path"]]

    def add_signal(self, lister):
        dir_path = QFileDialog.getExistingDirectory(self)
        lister.addRow(dir_path)
        return

    def remove_signal(self, lister):
        lister.removeSelectedRow()
        return

    def save_signal(self, list1, list2):

        name_list = ['ProjectDir', 'UnityDir']
        list = self.list_holder[:]   # copy

        ys = collections.OrderedDict()
        for i in range(len(name_list)):
            data = collections.OrderedDict()
            data["path"] = []
            for index in range(list[i].count()):
                data["path"].append(list[i].item(index).text())

            print(data["path"])

            ys[name_list[i]] = data

        fw = open('data/data.json', 'w')
        json.dump(ys, fw, indent=4)

        Global.printStatus("Saved.", 3000)

        return

    def get_unity_parent_path_list(self):
        return self.list_holder[1]

    def reflesh_signal(self):
        return