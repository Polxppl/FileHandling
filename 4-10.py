import csv

with open('clothing.csv', 'r', newline='') as csvfile:
  content = csv.reader(csvfile, delimiter=',')
  next(content, None)
  filtered = filter(lambda a: float(a[5]) < 60 and float(a[6]) < 40, content)
  print('\n'.join([','.join(row) for row in filtered]))

