import csv

print('GRAPHIC DESIGNERS')
print('=================')

with open('it_company.csv', 'r', newline='') as csvfile:
  content = csv.reader(csvfile, delimiter=',')
  filtered = filter(lambda a: a[2] == 'Graphic Designer', content)
  print('\n'.join([f'{row[0]} {row[1]}, {row[2]}' for row in filtered]))

