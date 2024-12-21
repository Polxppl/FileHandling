###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

def read_from_file(name):
   with open(name, "r", encoding="utf-8") as file:
      content = file.read()
   return content

email = read_from_file(email_file)

# regular expression pattern
# for amounts
pattern = r'€(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
  total += int(amount)


print('Total amount: ', total)


