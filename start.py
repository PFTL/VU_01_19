from PyQt5.QtWidgets import QApplication

from model.experiment import Experiment
from view.main_window import ScanWindow

exp = Experiment()
exp.load_config('experiment.yml')
exp.load_daq()

app = QApplication([])
scan_window = ScanWindow(exp)
scan_window.show()
app.exec_()
