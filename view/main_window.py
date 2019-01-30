from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from model.experiment import Experiment

exp = Experiment()
exp.load_config('experiment.yml')
exp.load_daq()

app = QApplication([])
window = QMainWindow()
uic.loadUi('main_window.ui', window)

def start_press():
    print('Start Press')

def stop_press():
    print('Stop Press')

window.start_button.clicked.connect(exp.do_scan)
window.stop_button.clicked.connect(stop_press)

window.show()
app.exec_()