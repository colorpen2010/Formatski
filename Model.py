import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import  QUrl,QStringListModel,Qt
from forms import Ui_MainWindow

def change():
    result=random.randint(0,9999)
    list.append(str(result))
    w.setStringList(list)

def slot(material):
    peremenaia=s.listView.currentIndex()
    kva=w.data(peremenaia,Qt.ItemDataRole.DisplayRole)
    print(kva)

s=Ui_MainWindow()
e=QApplication()
w=QStringListModel()

list=w.stringList()
list.append('9999')
w.setStringList(list)
q=QMainWindow()
s.setupUi(q)
s.listView.setModel(w)
s.listView_2.setModel(w)
model=s.listView.selectionModel()
model.selectionChanged.connect(slot)


s.pushButton.clicked.connect(change)
q.show()
e.exec()