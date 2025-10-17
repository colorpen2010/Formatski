import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QGraphicsScene
from PySide6.QtGui import QPen
from PySide6.QtCore import  QUrl,QStringListModel,Qt,QLineF,QRect
from forms_2 import Ui_MainWindow

s=Ui_MainWindow()
e=QApplication()
r=QGraphicsScene()
a=QLineF()
w=QPen()

rect_size=50,50

q=QMainWindow()
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



w.setColor("red")

s.setupUi(q)
s.graphicsView.setScene(r)
for b in rects:
 r.addRect(b)

q.setWindowTitle("Skylines Cities")

err=s.graphicsView.viewport().rect().topLeft()
print(s.graphicsView.mapToScene(err))
print(s.graphicsView.scene().sceneRect().width())

q.show()
e.exec()