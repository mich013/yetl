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


class Tables:
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
        return cls(filename, tables, object)

    def __repr__(self):
        return 'Message(filename={}, tables={}, object={})'.format(
            self.filename, self.tables, self.object)
    
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
        return cls(filename, tables, object)

    def __repr__(self):
        return 'Message(filename={}, tables={}, object={})'.format(
            self.filename, self.tables, self.object)
    

if __name__=="__main__":
    yaml = ruamel.yaml.YAML(typ='safe')
    yaml.register_class(Version)
    #yaml.register_class(Message)
    with open('etl.yaml') as fp:
        data = yaml.load(fp)
    print(data)