import os
import yaml



BASE_DIR = os.path.abspath(__file__)
print(BASE_DIR)
DIRNAME = os.path.dirname(__file__)
print(DIRNAME)
DIRNAME_2 = os.path.dirname(os.path.dirname(__file__))
print(DIRNAME_2)

config_file = os.path.join(DIRNAME_2, 'Config', 'experiment.yml')
print(config_file)
f = open(config_file, 'r')
data = yaml.load(f)
# print(data)
print(data['Scan']['start'], data['Scan']['stop'])