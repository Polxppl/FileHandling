def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('it_company.csv')

arr = file_content.splitlines()[1:-1]

filtered = list(filter(lambda a: a.split(',')[2] == 'Software Engineer', arr))

for row in range(0, len(filtered)):
   print(f'{row + 1}. {filtered[row]}')
