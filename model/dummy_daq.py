import random
from model import ur


class AnalogDaq:
    def __init__(self, port, resistance):
        self.port = port
        self.resistance = resistance

    def set_voltage(self, channel, voltage):
        pass

    def read_voltage(self, channel):
        value = random.random()*1023
        voltage = value/1023*ur('3.3V')
        return voltage

    def read_current(self, channel):
        voltage = self.read_voltage(channel)
        current = voltage/self.resistance
        return current

    def initialize(self):
        pass

    def finalize(self):
        pass


if __name__ == '__main__':
    resistance = ur('220ohm')
    analog_daq = AnalogDaq('/dev/ttyACM0', resistance)
    analog_daq.initialize()

    out_voltage = ur('3300mV')
    analog_daq.set_voltage(0, out_voltage)

    voltage = analog_daq.read_voltage(1)
    current = analog_daq.read_current(0)
    print(voltage)
    print(current.to('mA'))
    analog_daq.finalize()