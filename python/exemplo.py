from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout

app = QApplication()
base = QWidget()
layout = QVBoxLayout()

font = QFont()
font.setPixelSize(50)

label = QLabel('teste')
label.setFont(font)
label.setAlignment(Qt.AlignCenter)

botao = QPushButton('botão')
botao.setFont(font)

layout.addWidget(label)
layout.addWidget(botao)

base.setLayout(layout)
base.show()

app.exec()