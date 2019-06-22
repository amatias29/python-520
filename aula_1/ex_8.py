
import json

config = None
with open('config.json', 'r') as f:
	config = json.load(f)

print(config)

config['aula'] = 1

with open('config.json', 'w') as f:
	json.dump(config, f, indent=4)