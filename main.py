'''Python bindings for qt5.'''
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    '''Subclass extending QMainWindow for customization.'''

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.windowTitleChanged.connect(self.on_window_title_change)
        self.setWindowTitle('Learning Qt with PyQt')

        label = QLabel('Hi, this is my first Qt app!')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    # have to use this "decorater" if 'self' or 'cls' is not a arg for the a class method
    @staticmethod
    def on_window_title_change(event):
        '''Prints the new title.'''
        print(event)

APP = QApplication([])

WINDOW = MainWindow()

WINDOW.show()

APP.exec()  # exec() = exec_() in PyQt5
