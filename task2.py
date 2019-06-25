import subprocess
import sys
import json
import yaml


information = {
    'version': subprocess.check_output(
        ['python', '-V'], universal_newlines=True).split('\n')[0],
    'virtual_environment': subprocess.check_output(
        ['pyenv', 'version-name'], universal_newlines=True).split('\n')[0],
    'executable': sys.executable,
    'pip_location': subprocess.check_output(
        ['which', 'pip'], universal_newlines=True).split('\n')[0],
    'pythonpath': sys.path,
    'site-packages_location': next(p for p in sys.path if 'site-packages' in p)
}

# [:-1] - delete last empty string
modules = subprocess.check_output(
    ['pip', 'freeze'], universal_newlines=True).split('\n')[:-1]
dict_modules = {}
for module in modules:
    temp = module.split('==')
    dict_modules[temp[0]] = temp[1]

information['modules'] = dict_modules

with open('information.json', 'w') as file:
    json.dump(information, file, indent=4)

with open('information.yaml', 'w') as file:
    yaml.dump(information, file, default_flow_style=False, indent=4)
