import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow
from get_image import get_image


class MapsAPI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save.clicked.connect(self.show_map)

    # отображает картинку
    def show_map(self):
        ll, spn = '66,66', '0.005,0.005'
        get_image(ll, spn)

        self.label.setPixmap(QPixmap('map.png'))

    def coord_mas(self):
        '''
        return: self.coord, self.massh
        '''
        return self.coord.text(), self.massh.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapsAPI()
    ex.show()
    sys.exit(app.exec_())
