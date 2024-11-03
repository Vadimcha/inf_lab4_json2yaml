import json
import yaml

input_file = 'schedule.json'

with open(input_file, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

yaml_data = yaml.dump(json_data, allow_unicode=True)

print(yaml_data)
