'''Python bindings for qt5.'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    '''Subclass extending QMainWindow for customization.'''

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Learning Qt with PyQt')

        layout = QVBoxLayout()

        widgets = [
            QCheckBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit
        ]

        for widget in widgets:
            layout.addWidget(QLabel(widget.__doc__))
            layout.addWidget(widget())

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

APP = QApplication([])

WINDOW = MainWindow()

WINDOW.show()

APP.exec()  # exec() = exec_() in PyQt5
