original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

def write_to_file(name, content):
   with open(name, 'w') as file:
      content = file.write(content)


content = read_from_file(original_file)
write_to_file(target_file, content)
