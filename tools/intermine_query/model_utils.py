from intermine.webservice import Service

server = 'http://www.flymine.org/flymine/service'

service = Service(server)
model = service.model

def get_classes():
    return [(cl, cl, cl == 'Gene') for cl in model.classes.keys()]

def get_attributes(class_name):
    attrs = list()
    for field in model.get_class(class_name).fields:
        if hasattr(field.type_class, 'attributes'):
            cl = field.type_class
            for attr in cl.attributes + cl.fields:
                el = '.'.join([field.name, attr.name])
                attrs.append((el, el, False))
        else:
            el = field.name
            attrs.append((el, el, False))
    return attrs
