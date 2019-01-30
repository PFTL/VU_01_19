from time import sleep

import os
import yaml
import numpy as np
from model.analog_daq import AnalogDaq
from model import ur


class Experiment:
    def __init__(self):
        self.scan_running = False

    def load_config(self, filename):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        config_file = os.path.join(base_dir, 'Config', filename)
        f = open(config_file, 'r')
        self.config = yaml.load(f)
        f.close()

    def load_daq(self):
        port = self.config['DAQ']['port']
        resistance = self.config['DAQ']['resistance']
        resistance = ur(resistance)
        self.daq = AnalogDaq(port, resistance)
        self.daq.initialize()

    def do_scan(self):
        start = ur(self.config['Scan']['start'])
        stop = ur(self.config['Scan']['stop'])
        step = ur(self.config['Scan']['step'])
        num_points = (stop-start)/step
        num_points = round(num_points.m_as('')) + 1
        voltages = np.linspace(start.m_as('V'), stop.m_as('V'), num_points)
        channel_out = self.config['Scan']['channel_out']
        self.scan_data = []
        channel_in = self.config['Scan']['channel_in']
        delay = ur(self.config['Scan']['delay'])
        for voltage in voltages:
            self.scan_running = True
            voltage = voltage * ur('V')
            self.daq.set_voltage(channel_out, voltage)
            current = self.daq.read_current(channel_in)
            self.scan_data.append([voltage, current])
            sleep(delay.m_as('s'))
        self.scan_running = False

    def apply_voltage(self, channel, voltage):
        channel_out = self.config['Scan']['channel_out']

    def save_data(self):
        folder = self.config['Save']['folder']
        filename = self.config['Save']['filename']

        if not os.path.isdir(folder):
            os.makedirs(folder)

        base_file = os.path.join(folder, filename)
        i = 0
        full_file = base_file + '.txt'
        while os.path.isfile(full_file):
            full_file = base_file + str(i) + '.txt'
            i = i + 1

        print('Saving data to', full_file)
        f = open(full_file, 'w')
        header = "# User: {}\n".format(self.config['User']['name'])
        header += "# Data Points {}\n".format(len(self.scan_data))
        header += "# Voltage, Current\n"
        f.write(header)
        for data in self.scan_data:
            line = "{}, {}\n".format(data[0], data[1])
            f.write(line)
        f.close()

        metadata_file = full_file[:-3] + 'metadata'
        f = open(metadata_file, 'w')
        yaml.dump(self.config, f)
        f.close()

if __name__ == '__main__':
    import threading

    exp = Experiment()
    exp.load_config('experiment.yml')
    print(exp.config)
    print(exp.config['DAQ'])
    exp.load_daq()
    print('Starting Scan')
    t = threading.Thread(target=exp.do_scan)
    t.start()
    sleep(.5)
    while exp.scan_running:
        print("{:2.3f~} - {:2.3f~}".format(exp.scan_data[-1][0], exp.scan_data[-1][1].to('mA')))
        sleep(1)
    print('Scan Finished')
    exp.save_data()
