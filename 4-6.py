file_name = input('File name: ')

try:
  with open(file_name) as file:
    content = file.read()
    print('Number of lines: ', len(content.splitlines()))
    print('Number of characters: ', len(content))
    print('Number of words: ', len(content.split()))
except FileNotFoundError:
  print(f"Hey! The file {file_name} does not exist.")
