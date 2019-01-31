import os

import threading
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from model.experiment import Experiment
import pyqtgraph as pg


class ScanWindow(QMainWindow):
    def __init__(self, experiment):
        super().__init__(parent=None)
        base_folder = os.path.dirname(__file__)
        main_window_file = os.path.join(base_folder, 'main_window.ui')
        uic.loadUi(main_window_file, self)

        self.experiment = experiment

        self.start_button.clicked.connect(self.start_pressed)
        self.stop_button.clicked.connect(self.stop_pressed)

        self.out_channel_line.setText(str(self.experiment.config['Scan']['channel_out']))
        self.out_start_line.setText(self.experiment.config['Scan']['start'])
        self.out_stop_line.setText(self.experiment.config['Scan']['stop'])
        self.out_step_line.setText(self.experiment.config['Scan']['step'])

        self.in_channel_line.setText(str(self.experiment.config['Scan']['channel_in']))
        self.in_delay_line.setText(self.experiment.config['Scan']['delay'])

        self.plot_widget = pg.PlotWidget()
        self.plot = self.plot_widget.plot([0], [0])
        self.layout = self.centralwidget.layout()
        self.layout.addWidget(self.plot_widget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)

        self.action_Save.triggered.connect(self.experiment.save_data)
        self.action_Start.triggered.connect(self.start_pressed)
        self.action_Stop.triggered.connect(self.stop_pressed)

        self.progressBar.setValue(0)

    def update_plot(self):
        points_up_to_now = len(self.experiment.scan_data)
        progress_scan = points_up_to_now/self.experiment.num_points*100
        self.progressBar.setValue(progress_scan)
        x_data = []
        y_data = []
        for data in self.experiment.scan_data:
            x_data.append(data[0].m_as('V'))
            y_data.append(data[1].m_as('mA'))

        self.plot.setData(x_data, y_data)

    def start_pressed(self):
        new_scan_data = {
            'channel_out': self.out_channel_line.text(),
            'start': self.out_start_line.text(),
            'stop': self.out_stop_line.text(),
            'step': self.out_step_line.text(),
            'channel_in': self.in_channel_line.text(),
            'delay': self.in_delay_line.text()
        }
        print(new_scan_data)
        self.experiment.config['Scan'].update(new_scan_data)
        print(self.experiment.config)
        if not self.experiment.scan_running:
            t = threading.Thread(target=self.experiment.do_scan)
            t.start()
            print('Scan started')
            self.timer.start(500)
        else:
            print('Tried to start a second scan')

    def stop_pressed(self):
        self.experiment.keep_scanning = False
        print('Stop Pressed')

    def closeEvent(self, QCloseEvent):
        self.experiment.finalize()
        super().closeEvent(QCloseEvent)


if __name__ == "__main__":
    exp = Experiment()
    exp.load_config('experiment.yml')
    exp.load_daq()


    app = QApplication([])
    scan_window = ScanWindow(exp)
    scan_window.show()
    app.exec_()
