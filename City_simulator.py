import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QGraphicsScene, QWidget
from PySide6.QtGui import QPen, QStandardItemModel
from PySide6.QtCore import  QUrl,QStringListModel,Qt,QLineF,QRect, QPoint
from forms_2 import Ui_MainWindow
from ui_building_menu import  Ui_Form

z=QStandardItemModel(2,3)
s=Ui_MainWindow()
t=Ui_Form()
e=QApplication()
r=QGraphicsScene()
a=QLineF()
w=QPen()

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



w.setColor("red")

s.setupUi(q)
t.setupUi(f)
s.Building_menu.triggered.connect(building_menu)

z.setHorizontalHeaderLabels(["name","x","y"])
t.tableView.setEditTriggers(t.tableView.EditTrigger.NoEditTriggers)
t.tableView.setModel(z)

s.graphicsView.setScene(r)
for b in rects:
 r.addRect(b)

q.setWindowTitle("Skylines Cities")

err=s.graphicsView.viewport().rect().topLeft()
print(s.graphicsView.mapToScene(err))
print(s.graphicsView.scene().sceneRect().width())

q.show()
e.exec()