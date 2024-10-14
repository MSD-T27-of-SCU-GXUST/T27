from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

def read_text():
    text = line.text()
    print("输入框内容：", text)

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

line = QLineEdit()
layout.addWidget(line)

button = QPushButton('读取内容')
button.clicked.connect(read_text)
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec()