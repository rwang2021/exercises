import os
import json
from pprint import pprint

with open(os.path.expanduser('~')+r'\Desktop\Study\Python\Temp\pp.json','rt') as f:
    data = json.load(f)


print(data['ipV4Neighbors'][0]['address'])
print(data['ipV4Neighbors'][0]['hwAddress'])


output = {data['ipV4Neighbors'][0]['address']:data['ipV4Neighbors'][0]['hwAddress'],data['ipV4Neighbors'][1]['address']:data['ipV4Neighbors'][1]['hwAddress']}
print(output)
