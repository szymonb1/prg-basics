###
# Makes a copy of a text file
#

# file names
original_file = r'C:\Users\turni\Desktop\programowanie\prg-basics\prg-basics\08-FileHandling\healthy_lifestyle.txt'
target_file = r'C:\Users\turni\Desktop\programowanie\prg-basics\prg-basics\08-FileHandling\copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r') as f:
   content = f.read()

content = content.splitlines()


# write the content to the target file (copy)
with open(target_file, 'w') as f:
   for line in content:
      f.write(f"{line}\n")