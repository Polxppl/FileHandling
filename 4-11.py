

result = '\n'.join([', '.join([str(i), str(i * i), str(i * i * i)]) for i in range(1, 101)])

with open('4-11-result.txt', 'w') as file:
  file.write(result)

