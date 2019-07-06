import requests
import json

# We cannot use external libraries (like the `intermine` python client) here.

def create_model(registry):
    endpoint = '%s/service/model?format=json' % registry
    res = requests.get(url=endpoint)
    model = res.json()['model']
    return model

def get_classes(registry):
    model = create_model(registry)
    return [(cl['displayName'], cl['name'], cl == 'Gene')
            for cl in model['classes'].values()]

def get_attributes(registry, class_name):
    model = create_model(registry)
    attrs = list()
    for attr in model['classes'][class_name]['attributes'].values():
        el = attr['name']
        attrs.append((el, el, False))
    for cl in model['classes'][class_name]['collections'].values():
        for attr in model['classes'][cl['referencedType']]['attributes'].values():
            el = '.'.join([cl['name'], attr['name']])
            attrs.append((el, el, False))
    return attrs
