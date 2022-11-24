import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.start.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(randint(1, 7)):
            qp.drawEllipse(randint(10, 500), randint(10, 500), randint(10, 500), randint(10, 500))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
