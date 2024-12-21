def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

def write_to_file(name, content):
   with open(name, 'w') as file:
      content = file.write(content)

target_file = 'software_engineer.txt'
file_content = read_from_file('it_company.csv')

arr = file_content.splitlines()[1:-1]

filtered = list(filter(lambda a: a.split(',')[2] == 'Software Engineer', arr))

target_content = '\n'.join(filtered)


write_to_file(target_file, target_content)
