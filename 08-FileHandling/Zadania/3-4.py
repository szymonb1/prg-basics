###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = r'08-FileHandling\report.txt'

# read the content of email
with open(email_file, 'r', encoding="utf-8") as f:
   content = f.read()
# regular expression pattern
# for amounts

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(r'€(\d+)', content)
print(amounts)
# calculate the total purchases
total = sum([int(x) for x in amounts])

# print result
print(total)