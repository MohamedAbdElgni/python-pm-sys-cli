import json

data_path='data.json'

with open(data_path, 'r') as f:
    data = json.load(f)
    
    
print(data)