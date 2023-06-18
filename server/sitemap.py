import json
import yaml
import subprocess

json_file_path = '../data/sites.json'
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

yaml_data = yaml.dump(json_data)

yaml_file_path = '../../ysites/_data/sites.yml'
with open(yaml_file_path, 'w') as yaml_file:
    yaml_file.write(yaml_data)