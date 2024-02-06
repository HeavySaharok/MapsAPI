import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow
from get_image import get_image

# Программно настраиваемые переменные
# Размер карты:
limit_z = (21, 2)  # [0] - максимум, [1] - минимум
default_z = 10
size_step = 1
# Координаты:
default_coords = (37, 55)
coords_step = 1


class MapsAPI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save.clicked.connect(self.show_map)
        # Переменные с которыми взаимодействует клавиатура
        self.limit_z = limit_z
        self.z = default_z
        self.size_step = size_step
        self.coords = default_coords
        self.coords_step = coords_step

    # отображает картинку
    def show_map(self):
        ll, z = self.get_ll(), self.get_z()
        get_image(ll, z)

        self.label.setPixmap(QPixmap('map.png'))

    def coord_mas(self):
        '''
        return: self.coord, self.massh
        '''
        return self.coord.text(), self.massh.text()

    def get_ll(self):
        ll = f'{self.coords[0]},{self.coords[1]}'
        return ll

    def get_z(self):
        z = f'{self.z:.0f}'
        return z

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.z += self.size_step if self.z < self.limit_z[0] else 0
        if event.key() == Qt.Key_PageDown:
            self.z -= self.size_step if self.z > self.limit_z[1] else 0
        # Стрелки
        if event.key() == Qt.Key_Left:
            self.coords = (self.coords[0] - self.coords_step, self.coords[1])
        if event.key() == Qt.Key_Right:
            self.coords = (self.coords[0] + self.coords_step, self.coords[1])
        if event.key() == Qt.Key_Down:
            self.coords = (self.coords[0], self.coords[1] + self.coords_step)
        if event.key() == Qt.Key_Up:
            self.coords = (self.coords[0], self.coords[1] + self.coords_step)

        self.show_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapsAPI()
    ex.show()
    sys.exit(app.exec_())
