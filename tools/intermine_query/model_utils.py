import requests
import json

# We cannot use external libraries (like the `intermine` python client) here.

server = 'http://www.flymine.org/flymine/service'

endpoint = '%s/model?format=json' % server

res = requests.get(url=endpoint)
model = res.json()['model']

def get_classes():
    return [(cl['displayName'], cl['name'], cl == 'Gene')
            for cl in model['classes'].values()]

def get_attributes(class_name):
    attrs = list()
    for attr in model['classes'][class_name]['attributes'].values():
        el = attr['name']
        attrs.append((el, el, False))
    for cl in model['classes'][class_name]['collections'].values():
        for attr in model['classes'][cl['referencedType']]['attributes'].values():
            el = '.'.join([cl['name'], attr['name']])
            attrs.append((el, el, False))
    return attrs
