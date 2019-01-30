from controller.simple_daq import SimpleDaq
from pint import UnitRegistry


ur = UnitRegistry()


class AnalogDaq:
    def __init__(self, port, resistance):
        self.port = port
        self.resistance = resistance

    def set_voltage(self, channel, voltage):
        volts_out = voltage.m_as('V')
        value = int(volts_out*4095/3.3)
        self.daq.set_analog_value(channel, value)

    def read_voltage(self, channel):
        value = self.daq.get_analog_value(channel)
        voltage = value/1023*ur('3.3V')
        return voltage

    def read_current(self, channel):
        voltage = self.read_voltage(channel)
        current = voltage/self.resistance
        return current

    def initialize(self):
        self.daq = SimpleDaq(self.port)

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