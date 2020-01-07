'''Python bindings for qt5.'''
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    '''Subclass extending QMainWindow for customization.'''

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Learning Qt with PyQt')

        label = QLabel('Hi, this is my first Qt app!')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    def contextMenuEvent(self, event):
        '''Handle right-click menu event.'''
        print('I wont show Context Menu')
        super(MainWindow, self).contextMenuEvent(event)

APP = QApplication([])

WINDOW = MainWindow()

WINDOW.show()

APP.exec()  # exec() = exec_() in PyQt5
