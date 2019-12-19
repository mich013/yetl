
import random
import sys
import ruamel.yaml

class ListPick():
    def __init__(self, name=None, items=None):
        self.name=name
        self.items=items
        

    @classmethod
    def from_yaml(cls, constructor, node):
        for m in constructor.construct_yaml_map(node):
            pass
        return cls(m['Name'], m['Items'])

    def __repr__(self):
        return 'Version(name={.name}, items={.items})'.format(self, self)

class CsvGen():
    def __init__(self, header=None, count=None, row=None, tablename=None):
        self.header=header
        self.count=count
        self.row=row
        self.tablename=tablename

    @classmethod
    def from_yaml(cls, constructor, node):
        for m in constructor.construct_yaml_map(node):
            pass
        return cls(m['Header'], m['Count'], m['Row'], m['TableName'])

    def __repr__(self):
        return 'Version(header={.header}, count={.count}, row={.row}, tablenake={.tablename})'.format(self, self, self, self)




# produce = ["Apple",
#           "Grapes",
#           "Almonds",
#           "Walnuts",
#           "Pears",
#           "Oranges"]
# 
# count = 500
# fname = "input.csv"
# with open(fname, "w+") as f:
#     f.write("Produce,Qty,Price\n")
#     for i in range(0, count):
#         p = produce[random.randint(0, len(produce)-1)]
#         qty = random.randint(1,10)
#         price = random.uniform(1.5, 10.0)
#         f.write('"{}",{},{}\n'.format(p,qty,price))

if __name__=="__main__":
   yaml = ruamel.yaml.YAML(typ='safe')
   yaml.register_class(CsvGen)
   yaml.register_class(ListPick)
   #yaml.register_class(Message)
   with open('CsvGen.yml') as fp:
       data = yaml.load(fp)
   print(type(data))
    