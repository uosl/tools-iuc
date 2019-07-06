import requests
import json

# We cannot use external libraries (like the `intermine` python client) here.

# Note: The functions here don't get run when their input (defined in the XML)
# changes, unless a `repeat` is removed or added. This results in a caching bug
# that we can't fix; our selections won't get updated when the `registry` or
# `class_name` changes.

last_registry = None

model_cache = None

def create_model(registry):
    global model_cache
    global last_registry

    if model_cache and last_registry == registry:
        return model_cache

    endpoint = '%s/service/model?format=json' % registry
    res = requests.get(url=endpoint)
    model = res.json()['model']

    model_cache = model
    last_registry = registry

    return model

classes_cache = None

def get_classes(registry):
    global classes_cache

    if classes_cache and last_registry == registry:
        return classes_cache

    model = create_model(registry)

    classes = [(cl['displayName'], cl['name'], cl['name'] == 'Gene') for cl in model['classes'].values()]

    classes_cache = classes

    return classes

last_class_name = None

attributes_cache = None

def get_attributes(registry, class_name):
    global last_class_name
    global attributes_cache

    if attributes_cache and last_registry == registry and last_class_name == class_name:
        return attributes_cache

    model = create_model(registry)

    attrs = list()

    for attr in model['classes'][class_name]['attributes'].values():
        el = attr['name']
        attrs.append((el, el, el == 'symbol'))

    for cl in model['classes'][class_name]['collections'].values():
        for attr in model['classes'][cl['referencedType']]['attributes'].values():
            el = '.'.join([cl['name'], attr['name']])
            attrs.append((el, el, False))

    attributes_cache = attrs
    last_class_name = class_name

    return attrs
