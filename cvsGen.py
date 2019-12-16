
import random

produce = ["Apple",
          "Grapes",
          "Almonds",
          "Walnuts",
          "Pears",
          "Oranges"]

count = 500
fname = "input.csv"
with open(fname, "w+") as f:
    f.write("Produce,Qty,Price\n")
    for i in range(0, count):
        p = produce[random.randint(0, len(produce)-1)]
        qty = random.randint(1,10)
        price = random.uniform(1.5, 10.0)
        f.write('"{}",{},{}\n'.format(p,qty,price))  