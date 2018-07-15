import xml.etree.ElementTree as etree
import json


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.loads(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parse_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('wml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filerath):
    factory = None
    try:
        factory = connection_factory(filerath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    sqlite_factory = connect_to('data/mydata.sq3')
    print()

    xml_factory = connect_to('data/madata.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{} = {}]".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: { }'.format(liar.find('firstName').text))
        print('first name: { }'.format(liar.find('lastName').text))
        [print('phone number ({})'.format(p.attrib['type']),
               p.text) for p in liar.find('phoneNumbers')]
        print()

    json_factory = connect_to('data/dount.json')
    json_data = json_factory.parsed_data
    print('found: {} dounts'.format(len(json_data)))
    for dount in json_data:
        print('name: {}'.format(dount['ppu']))
        [print('price: ${}'.format(t['id'], t['type']))
         for t in dount['topping']]


if __name__ == '__main__':
    main()
