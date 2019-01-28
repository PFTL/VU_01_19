import serial
from time import sleep

class Device:
    def __init__(self, port):
        self.port = port
        self.rsc = None

    def initialize(self):
        self.rsc = serial.Serial(self.port)
        sleep(0.5)

    def idn(self):
        """Get the identification string of the device"""
        return self.query('IDN')

    def read_analog(self, channel):
        command = 'IN:CH{}'.format(channel)
        return int(self.query(command))

    def set_analog(self, channel, value):
        if value > 4095:
            raise Exception('Value cant exceed 4095')

        command = 'OUT:CH{}:{}'.format(channel, value)
        self.write(command)
        sleep(0.1)

    def write(self, command):
        if self.rsc is None:
            raise Exception('Device not initialized. Please run initialize first.')

        command = command + '\n'
        command = command.encode('ascii')
        self.rsc.write(command)

    def query(self, command):
        self.write(command)
        return self.rsc.readline().decode('ascii').strip()

if __name__ == '__main__':
    dev = Device('/dev/ttyACM0')
    dev.initialize()
    print(dev.idn())
    dev.set_analog(0, 5000)
    print(dev.read_analog(0))
    dev.set_analog(0, 0)
    values = []
    for i in range(10):
        dev.set_analog(0, i*400)
        values.append(dev.read_analog(0))

    print(values)
