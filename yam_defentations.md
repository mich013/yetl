# Yaml Defentation

## CSV table def

yaml code

--- !csvLoad
InputTable: input.csv
Columns:
- Column:
  Name: A
  Type: string
  Transform: upper
- Column:
  Name: B
  Type: int
- Column
  Name: C
  Type: float
