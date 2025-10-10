import random

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QPixmap, QCursor
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer
from PySide6.QtCore import  QUrl
from forms import Ui_MainWindow

def call_back():
    if s.progressBar.value()<=0:
        f.play()
        print("+40 exp +15 gold")
        return
    print("er")
    s.progressBar.setValue(s.progressBar.value()-5)
    d.play()
    s.pushButton.setGeometry(random.randint(0,500), random.randint(0,500), 70, 25)

s=Ui_MainWindow()
e=QApplication()
x=QUrl.fromLocalFile(r"C:\Users\GmodHunter\PycharmProjects\Formatski\sounds\slash_hit.wav")

z=QUrl.fromLocalFile(r"C:\Users\GmodHunter\PycharmProjects\Formatski\sounds\Splat.wav")
d=QSoundEffect(source=z)
f=QSoundEffect(source=x)

d.setVolume(0.8)
w=QPixmap(r"C:\Users\GmodHunter\PycharmProjects\Formatski\images\Knife.png")
a=QCursor(w,1,1)
q=QMainWindow()
s.setupUi(q)
s.pushButton.clicked.connect(call_back)
s.pushButton.setCursor(a)
q.show()
e.exec()

