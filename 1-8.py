def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')

print('Number of words: ', len(file_content.split(' ')))
print(file_content)
