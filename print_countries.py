###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    i = 1
    for line in file:
        print(f'{i}. {line}', end="")
        i += 1
