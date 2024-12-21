import re
def read_from_file(name):
   with open(name, "r", encoding="utf-8") as file:
      content = file.read()
   return content

content = read_from_file('files.txt')

filtered = re.findall(r'^.*\.\w{4}$', content, re.MULTILINE)

print(filtered)
