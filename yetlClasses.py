import yaml
import petl as etl

class CsvTable(yaml.YAMLObject):
    yaml_tag = u'!CsvTable'
    def __init__(self, input_table, columns):
        self.A = None
        self.table = None
        self.input_table = input_table
        self.columns = columns
    def load(self):
        self.table =  etl.fromcsv(self.InputTable)
        for Column in o.Columns:
            if "Type" in Column:
                print(Column)
                self.table = etl.convert(self.table, Column["Column"], eval(Column["Type"]) )     
            if "Convert" in Column:
                print(Column)
                self.table = etl.convert(self.table, Column["Column"], Column["Convert"])
            if "AddField" in Column:
                print(Column)
                self.table = etl.addfield(self.table, Column["Column"], eval(Column["AddField"]))
    def look(self):
        print(etl.look(self.table))
    def wrap(self, l):
        self.table = etl.wrap(l)
    def print(self):
        print(self.table)
        
if __name__=="__main__":
    print("in init")
    y = ""
    with open("input.yml") as f:
        y = f.read()  
    for o in yaml.load_all(y):
        print(o)
    o.load()
    o.look()
    o.print()
       
    
    a = 1
    # print(o, type(o))
