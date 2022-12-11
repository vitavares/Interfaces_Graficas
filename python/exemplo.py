from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication()

font = QFont()
font.setPixelSize(50)

label = QLabel('Botão')
label.setFont(font)
label.show()

app.exec()