###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = r'prg-basics\08-FileHandling\report.txt'

# read the content of email
with open(email_file, 'r', encoding="utf-8") as f:
   content = f.read()
# regular expression pattern
# for amounts

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(r'€\s*\d+', content)
print(amounts)
# calculate the total purchases
total = 0
for amount in amounts:
   total += int(amount[1:])

# print result
print(total)