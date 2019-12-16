import sys
import ruamel.yaml


yaml_str = """
- ModuleName: myTestModule
- Version: 1.0
- ModuleNumbers: [96,97,98,99]


- !Message
  Name: AO3_
  DLC: 8
  Signal1:
    Name: Temperature
    Length: 16
  Signal2:
    Name: AnalogOut3
    Length: 16
    SignalGroup1:  #Comment
       Name: app_fcex
       Type: Bitfield
       Signal1:
           Name: drive_ready
           Length: 1
       Signal2:
           Name: error_active
           Length: 1
       Signal3:
           Name: warning_active
           Length: 1
  Signal3:
    Name: Temperatur 2
    Length: 8
    ValueTable:
       Name: TempStates
       items:
       - !Item
         Name: INIT
         Value: 1
       - !Item
         Name: RUN
         Value: 2
       - !Item
         Name: DONE
         Value: 3
       - !Item
         Name: ERROR
         Value: 4
- !Message
  name: AO2_
  object: RX2
  DLC: 8"""

class Item:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    @classmethod
    def from_yaml(cls, constructor, node):
        for m in constructor.construct_yaml_map(node):
            pass
        return cls(m['Major'], m['Minor'], m['Patch'])

    def __repr__(self):
        return 'Version(major={.major}, minor={.minor}, patch={.patch})'.format(self, self)

class Message:
    def __init__(self, name=None, DLC=None, object=None, signals=None):
        self.name = name
        self.dlc = DLC
        self.object = object
        self.signals = [] if signals is None else signals

    @classmethod
    def from_yaml(cls, constructor, node):
        for m in constructor.construct_yaml_map(node):
            pass
        if 'Name' in m:
            name = m['Name']
        elif 'name' in m:
            name = m['name']
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

yaml = ruamel.yaml.YAML(typ='safe')
yaml.register_class(Item)
yaml.register_class(Message)
data = yaml.load(yaml_str)

aa = 1
    