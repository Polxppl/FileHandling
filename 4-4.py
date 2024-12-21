
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content


content = read_from_file('it_company.csv').splitlines()

line = 0
while line < len(content):
  print('\n'.join(content[line:line + 5]))
  line += 5
  input('Press Enter key...')


