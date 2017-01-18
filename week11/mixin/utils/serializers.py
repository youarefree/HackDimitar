import json
import xml.etree.ElementTree as ET
# from json import JSONEncoder


class Jsonable:
    serializable_types = (dict, list, tuple, bool, None, float, int)

    def to_json(self):
        data = {
            'dict': self.__dict__,
            'classname': self.__class__.__name__
        }

        for k, v in self.__dict__.items():
            if type(v) in self.serializable_types:
                data['dict'][k] = v

            if isinstance(v, Jsonable):
                data['dict'][k] = v

        # with open("Jfile.json", 'w') as outfile:
        return json.dumps(data, indent=4)

    # def to_json(self):
    #     with open("Jfile.json", 'w') as outfile:
    #         return json.dump(self.to_before_json(), outfile, indent=4)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        classname = data.get('classname', None)

        if cls.__name__ != classname:
            raise ValueError('{} != {}'.format(cls.__name__, classname))

        return cls(**data['dict'])


class Xmable:
    def to_xml(self):
        classname = self.__class__.__name__
        root = ET.Element(classname)

        for k, v in self.__dict__.items():
            kelement = ET.SubElement(root, k)
            kelement.text = str(v)

        return ET.tostring(root).decode('utf8')

    @classmethod
    def from_xml(cls, xml_str):
        root = ET.fromstring(xml_str)

        if root.tag != cls.__name__:
            raise ValueError

            data = {}

        for child in root:
            data[child.tag] = child.text

        return cls(**data)


class Panda(Jsonable, Xmable):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


panda = Panda(name="Ivo", age=18)
json_string = panda.to_json()
xml_sring = panda.to_xml(panda)
print(json_string)
# print(p1)

