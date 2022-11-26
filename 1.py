import json
data = {}
data['people'] = []
data['people'].append({
    'name': 'Misha',
    'website': 'pythonist.ru',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Roma',
    'website': 'pythonist.ru',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'pythonist.ru',
    'from': 'Alabama'
})
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

data = json.load(json_file)
for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
