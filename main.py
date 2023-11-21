import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor
from UI import Ui_MainWindow


class Balls(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.circle()
            self.qp.end()

    def circle(self):
        self.random = random.randint(1, 600)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(random.randint(1, 800), random.randint(1, 600), self.random, self.random)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Balls()
    ex.show()
    sys.exit(app.exec_())
