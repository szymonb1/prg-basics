###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = r'prg-basics\08-FileHandling\it_company.csv'
position_file = r'prg-basics\08-FileHandling\software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r') as ef:
   with open(position_file, 'w') as pf:
      for line in ef:
         if job_title in line:
            pf.write(line)