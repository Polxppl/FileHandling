import re

text = input('Enter text: ')

result = re.findall(r'[eyuioa]', text)

print('Vowels count: ', len(result))
