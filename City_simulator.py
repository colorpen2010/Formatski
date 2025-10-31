import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QGraphicsScene, QWidget
from PySide6.QtGui import QPen, QStandardItemModel,QStandardItem
from PySide6.QtCore import  QUrl,QStringListModel,Qt,QLineF,QRect, QPoint
from forms_2 import Ui_MainWindow
from ui_building_menu import  Ui_Form

z=QStandardItemModel(0,3)
s=Ui_MainWindow()
t=Ui_Form()
e=QApplication()
r=QGraphicsScene()
a=QLineF()
w=QPen()
item=QStandardItem()

def row_adder(name,x,y):
    row = [
        QStandardItem(str(name)),
        QStandardItem(str(x)),
        QStandardItem(str(y))
    ]
    z.appendRow(row)

row_adder('house',3,4)
row_adder("shop",3,3)

rect_size=50,50

q=QMainWindow()
f=QWidget()
rects=[]
print(int(r.sceneRect().left()))
for b in range(int(-550),151,rect_size[0]):
    for by in range(-525,1,rect_size[1]):
        rects.append(QRect(b,by,*rect_size))

# rects.append(QRect())
# (-150,-100,50,50)
# (-100,-50,50,50)
# (-50,0,50,50)
# d.setRect(-0,50,50,50)
# d.setRect(50,100,50,50)


def building_menu():
    cifri=q.geometry()
    print(cifri)

    f.move(cifri.right()+5,cifri.top()-30)
    f.show()


def on_row_selected(current):
    row = current.row()
    name = z.item(row, 0)
    x = z.item(row, 1)
    y = z.item(row, 2)
    print(name.text())
    t.lineEdit.setText(name.text())
    t.spinBox.setValue(int(x.text()))
    t.spinBox_2.setValue(int(y.text()))


w.setColor("red")

s.setupUi(q)
t.setupUi(f)
s.Building_menu.triggered.connect(building_menu)

z.setHorizontalHeaderLabels(["name","x","y"])
t.tableView.setEditTriggers(t.tableView.EditTrigger.NoEditTriggers)

t.tableView.setModel(z)

t.tableView.selectionModel().currentChanged.connect(on_row_selected)

s.graphicsView.setScene(r)
for b in rects:
 r.addRect(b)


q.setWindowTitle("Skylines Cities")

err=s.graphicsView.viewport().rect().topLeft()
print(s.graphicsView.mapToScene(err))
print(s.graphicsView.scene().sceneRect().width())

q.show()
e.exec()