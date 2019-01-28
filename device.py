from time import sleep

import serial


dev = serial.Serial('/dev/ttyACM0')
sleep(.25)
dev.write(b'IDN\n')
answer = dev.readline()
print(answer)
values = []
for i in range(20):
    value = i*200
    command = 'OUT:CH0:{}\n'.format(value)
    command = command.encode('ascii')
    dev.write(command)
    sleep(1)
    dev.write(b'IN:CH0\n')
    value = int(dev.readline())
    print(value)
    values.append(value)

print(values)

dev.close()
