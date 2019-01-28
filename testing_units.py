import pint
ur = pint.UnitRegistry()
base = 5 * ur('cm')
height = ur('3in')
area = base * height / 2
print(area)
print(area.to('cm**2'))
print(area.to('in**2'))

current = 2 * ur('A')
resistance = 3 * ur('ohm')

voltage = current*resistance
print(voltage.to('pV'))
