###
# Prints employees employed in a specified position.
#

# Employee List
file_name = r'C:\Users\turni\Desktop\programowanie\prg-basics\prg-basics\08-FileHandling\it_company.txt'

# Position
job_title = 'Software Engineer'

with open(file_name, 'r') as f:
   for line in f:
      if job_title in line:
         print(line)