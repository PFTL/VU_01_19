import threading
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
    t = threading.Thread(target=exp.do_scan)
    t.start()
    window.status_line.setText('Scan Running')

def stop_press():
    print('Stop Press')



window.start_button.clicked.connect(start_press)
window.stop_button.clicked.connect(stop_press)

window.show()
app.exec_()