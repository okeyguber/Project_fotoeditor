import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QProgressBar,
                             QApplication, QLabel, QFileDialog)
from PyQt5 import QtWidgets
from PIL import Image
from PyQt5.QtGui import QPixmap, QIcon
import numpy as np
import os
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QInputDialog

fname = ''
ex2 = ''


class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1 экран.ui', self)
        self.setWindowIcon(QIcon('icon1.png'))

        hbox = QHBoxLayout(self)
        self.pixmap = QPixmap('1423036688 (1).jpg')

        lbl = QLabel(self.label_pic)
        lbl.setPixmap(self.pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.btn_browse.clicked.connect(self.browse_folder)
        self.btn_next.clicked.connect(self.next_window)

    def browse_folder(self):
        global fname
        fname = QFileDialog.getOpenFileName(self, 'Open file', './~')[0]
        try:
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
                f.close()
        except:
            pass
        return fname

    def next_window(self):
        global ex2
        self.window = QtWidgets.QMainWindow()
        ex2 = Window2()
        ex.hide()
        ex2.show()


class Window2(QMainWindow):
    def __init__(self):
        global fname
        super().__init__()
        uic.loadUi('2 экран.ui', self)
        self.f = Image.open(fname)
        self.setWindowIcon(QIcon('icon1.png'))

        hbox_file = QHBoxLayout(self)
        self.pixmap_file = QPixmap(fname)
        self.lbl_file = QLabel(self.lbl_file)
        self.lbl_file.setPixmap(self.pixmap_file)
        hbox_file.addWidget(self.lbl_file)
        self.setLayout(hbox_file)

        hbox_stereo = QHBoxLayout(self)
        self.pixmap_stereo = QPixmap('стерео.jpg')
        self.lbl_stereo = QLabel(self.label_stereo)
        self.lbl_stereo.setPixmap(self.pixmap_stereo)
        hbox_stereo.addWidget(self.lbl_stereo)
        self.setLayout(hbox_stereo)

        hbox_negatiff = QHBoxLayout(self)
        self.pixmap_negatiff = QPixmap('negatiff.jpg')
        self.lbl_negatiff = QLabel(self.label_negatiff)
        self.lbl_negatiff.setPixmap(self.pixmap_negatiff)
        hbox_negatiff.addWidget(self.lbl_negatiff)
        self.setLayout(hbox_negatiff)

        hbox_bandw = QHBoxLayout(self)
        self.pixmap_bandw = QPixmap('bandw.jpg')
        self.lbl_bandw = QLabel(self.label_bandw)
        self.lbl_bandw.setPixmap(self.pixmap_bandw)
        hbox_bandw.addWidget(self.lbl_bandw)
        self.setLayout(hbox_bandw)

        hbox_dark = QHBoxLayout(self)
        self.pixmap_dark = QPixmap('dark.jpg')
        self.lbl_dark = QLabel(self.label_dark)
        self.lbl_dark.setPixmap(self.pixmap_dark)
        hbox_dark.addWidget(self.lbl_dark)
        self.setLayout(hbox_dark)

        hbox_light = QHBoxLayout(self)
        self.pixmap_light = QPixmap('light.jpg')
        self.lbl_light = QLabel(self.label_light)
        self.lbl_light.setPixmap(self.pixmap_light)
        hbox_light.addWidget(self.lbl_light)
        self.setLayout(hbox_light)

        self.btn_stereo.clicked.connect(self.stereo)
        self.btn_negatiff.clicked.connect(self.negatiff)
        self.btn_bandw.clicked.connect(self.bandw)
        self.btn_dark.clicked.connect(self.dark)
        self.btn_light.clicked.connect(self.light)
        self.btn_save.clicked.connect(self.save)
        self.btn_left.clicked.connect(self.povorot_left)
        self.btn_right.clicked.connect(self.povorot_right)
        self.btn_ver.clicked.connect(self.otr_ver)
        self.btn_gor.clicked.connect(self.otr_gor)

    def stereo(self):
        self.f = Image.open(fname)
        pixels = self.f.load()
        x, y = self.f.size
        newImage = Image.new('RGB', (x, y), (0, 0, 0))
        pixels2 = newImage.load()
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels2[i, j] = r, 0, 0
                pixels[i, j] = 0, g, b
        for i in range(10, x):
            for j in range(y):
                r, g, b = pixels[i, j]
                r2, g2, b2 = pixels2[i - 10, j]
                pixels[i, j] = r2, g, b
        self.f.save('запас.jpg')
        self.pixmap_file = QPixmap('запас.jpg')
        self.lbl_file.setPixmap(self.pixmap_file)

    def negatiff(self):
        self.f = Image.open(fname)
        pixels = self.f.load()
        x, y = self.f.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 255 - r, 255 - g, 255 - b
        self.f.save('запас.jpg')
        self.pixmap_file = QPixmap('запас.jpg')
        self.lbl_file.setPixmap(self.pixmap_file)

    def bandw(self):
        self.f = Image.open(fname)
        arr = np.asarray(self.f, dtype='uint8')
        k = np.array([[[0.2989, 0.587, 0.114]]])
        sums = np.round(np.sum(arr * k, axis=2)).astype(np.uint8)
        arr2 = np.repeat(sums, 3).reshape(arr.shape)
        self.f = Image.fromarray(arr2)
        self.f.save('запас.jpg')
        self.pixmap_file = QPixmap('запас.jpg')
        self.lbl_file.setPixmap(self.pixmap_file)

    def dark(self):
        self.f = Image.open(fname)
        pixels = self.f.load()
        x, y = self.f.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r - 100, g - 100, b - 100
        self.f.save('запас.jpg')
        self.pixmap_file = QPixmap('запас.jpg')
        self.lbl_file.setPixmap(self.pixmap_file)

    def light(self):
        self.f = Image.open(fname)
        pixels = self.f.load()
        x, y = self.f.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r + 50, g + 50, b + 50
        self.f.save('запас.jpg')
        self.pixmap_file = QPixmap('запас.jpg')
        self.lbl_file.setPixmap(self.pixmap_file)

    def save(self):
        global ex2
        os.remove('запас.jpg')
        self.f.save('new_image.jpg')
        self.window = QtWidgets.QMainWindow()
        self.ex3 = Window3()
        ex2.hide()
        self.ex3.show()

    def povorot_left(self):
        self.f = Image.open('запас.jpg')
        self.f.transpose(Image.ROTATE_90).save('запас.jpg')
        self.pixmap_file = QPixmap('запас.jpg')
        self.lbl_file.setPixmap(self.pixmap_file)

    def povorot_right(self):
        self.f = Image.open('запас.jpg')
        self.f.transpose(Image.ROTATE_270).save('запас.jpg')
        self.pixmap_file = QPixmap('запас.jpg')
        self.lbl_file.setPixmap(self.pixmap_file)

    def otr_ver(self):
        self.f = Image.open('запас.jpg')
        self.f.transpose(Image.FLIP_LEFT_RIGHT).save('запас.jpg')
        self.pixmap_file = QPixmap('запас.jpg')
        self.lbl_file.setPixmap(self.pixmap_file)

    def otr_gor(self):
        self.f = Image.open('запас.jpg')
        self.f.transpose(Image.FLIP_TOP_BOTTOM).save('запас.jpg')
        self.pixmap_file = QPixmap('запас.jpg')
        self.lbl_file.setPixmap(self.pixmap_file)


class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('3 экран.ui', self)
        self.setWindowIcon(QIcon('icon1.png'))

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(110, 220, 531, 30)

        self.btn_save.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn_save.setText('Сохранено!')
            self.label.setText('Готово! Спасибо что были с нами:3')
            return

        self.step = self.step + 10
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)
            self.btn_save.setText('Загрузка...')


app = QApplication(sys.argv)
ex = Window1()
ex.show()
sys.exit(app.exec_())
