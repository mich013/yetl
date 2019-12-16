import sys
import ruamel.yaml

class Version:
    def __init__(self, major=None, minor=None, patch=None):
        self.major=major
        self.minor=minor
        self.patch=patch

    @classmethod
    def from_yaml(cls, constructor, node):
        for m in constructor.construct_yaml_map(node):
            pass
        return cls(m['Major'], m['Minor'], m['Patch'])

    def __repr__(self):
        return 'Version(major={.major}, minor={.minor}, patch={.patch})'.format(self, self, self)

class Tables:
    def __init__(self, major=None, minor=None, patch=None):
        self.major=major
        self.minor=minor
        self.patch=patch

    @classmethod
    def from_yaml(cls, constructor, node):
        for m in constructor.construct_yaml_map(node):
            pass
        return cls(m['Major'], m['Minor'], m['Patch'])

    def __repr__(self):
        return 'Version(major={.major}, minor={.minor}, patch={.patch})'.format(self, self, self)


class CsvTable:
    def __init__(self, filename=None, Tables=None, object=None):
        self.filename = filename
        self.tables = [] if tables is None else tables
        self.object = object
        

    @classmethod
    def from_yaml(cls, constructor, node):
        for m in constructor.construct_yaml_map(node):
            pass
        if 'Name' in m:
            filename = m['FileName']
        elif 'columns' in m:
            columns = m['Columns']
        else:
            name = None
        object = m['object'] if 'object' in m else None
        if 'DLC' in m:
            dlc = m['DLC']
        else:
            dlc = None
        if 'signals' in m:
            signals = m['signals']
        elif 'Signal1' in m:
            x = 1
            signals = []
            while True:
                name = "Signal{}".format(x)
                try:
                    signals.append(m[name])
                except KeyError:
                    break
                x += 1
        else:
            signals = None
        return cls(name, dlc, object, signals)

    def __repr__(self):
        return 'Message(name={}, DLC={}, object={}, signals{})'.format(
            self.name, self.dlc, self.object, '[...]' if self.signals else '[]',
        )

if __name__=="__main__":
    yaml = ruamel.yaml.YAML(typ='safe')
    yaml.register_class(Version)
    #yaml.register_class(Message)
    with open('etl.yaml') as fp:
        data = yaml.load(fp)
    print(data)