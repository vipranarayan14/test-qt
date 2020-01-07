from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Learning Qt with PyQt')

        label = QLabel('Hi, this is my first Qt app!')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()  # exec() = exec_() in PyQt5
