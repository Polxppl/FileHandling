import csv


def read_file(name):
  with open('books.csv', 'r', newline='') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    next(content, None)
    return list(content)


def div_generes(content):
  generes = {}
  for book in content:
    if book[2] in generes:
      generes[book[2]].append(book)
    else:
      generes[book[2]] = [book]
  return generes


def name_to_filename(str):
  return f'{str.lower().replace('-', '_')}.txt'


content = read_file('books.csv')
generes = div_generes(content)

for genere in generes:
  with open(name_to_filename(genere), 'w') as file:
    file.write('\n'.join([','.join(cell) for cell in generes[genere]]))
