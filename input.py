from PyQt5.QtCore import Qt
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel

# Программно настраиваемые переменные
# Размер карты:
limit_size = (100, 0.001)  # [0] - максимум, [1] - минимум
default_size = 0.5
size_step = 0.001
# Координаты:
default_coords = (0, 0)
coords_step = 1

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Инпут')

        self.coordsLable = QLabel(self)
        self.coordsLable.setText(f"""Размер: 12312312312312312332
Координаты:123123123123123123123""")
        self.coordsLable.move(30, 30)

        # Переменные с которыми взаимодействует клавиатура
        self.limit_size = limit_size
        self.size = default_size
        self.size_step = size_step
        self.coords = default_coords
        self.coords_step = coords_step

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.size += self.size_step if self.size < self.limit_size[0] else 0
        if event.key() == Qt.Key_PageDown:
            self.size -= self.size_step if self.size > self.limit_size[1] else 0
        # Стрелки
        if event.key() == Qt.Key_Left:
            self.coords = (self.coords[0] - self.coords_step, self.coords[1])
        if event.key() == Qt.Key_Right:
            self.coords = (self.coords[0] + self.coords_step, self.coords[1])
        if event.key() == Qt.Key_Down:
            self.coords = (self.coords[0], self.coords[1] + self.coords_step)
        if event.key() == Qt.Key_Up:
            self.coords = (self.coords[0], self.coords[1] + self.coords_step)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
