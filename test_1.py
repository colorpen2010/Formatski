from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QGraphicsScene, QWidget

from forms import Ui_MainWindow
from ui_building_menu import  Ui_Form

s=Ui_MainWindow()
r=Ui_Form()
e=QApplication()
q=QMainWindow()
f=QWidget()

s.setupUi(f)
r.setupUi(q)

f.show()
q.show()
e.exec()