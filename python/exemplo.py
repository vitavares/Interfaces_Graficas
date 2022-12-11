from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow

app = QApplication()
window = QMainWindow()
base = QWidget()
layout = QVBoxLayout()

font = QFont()
font.setPixelSize(45)

label = QLabel('Botões')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)


b1 = QPushButton('b1')
b2 = QPushButton('b2')
b3 = QPushButton('b3')
b4 = QPushButton('b4')



layout.addWidget(label)
layout.addWidget(b1)
layout.addWidget(b2)
layout.addWidget(b3)
layout.addWidget(b4)


base.setLayout(layout)

window.setCentralWidget(base)

menu = window.menuBar()
arquivo_menu = menu.addMenu('Arquivo')
action = QAction('print')
arquivo_menu.addAction(action)

window.show()

app.exec()