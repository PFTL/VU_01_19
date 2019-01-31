import threading
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from model.experiment import Experiment


class ScanWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        uic.loadUi('main_window.ui', self)

        self.start_button.clicked.connect(self.start_pressed)
        self.stop_button.clicked.connect(self.stop_pressed)

    def start_pressed(self):
        print('Start Pressed')

    def stop_pressed(self):
        print('Stop Pressed')


if __name__ == "__main__":
    exp = Experiment()
    exp.load_config('experiment.yml')
    exp.load_daq()


    app = QApplication([])
    scan_window = ScanWindow()
    scan_window.show()
    app.exec_()
