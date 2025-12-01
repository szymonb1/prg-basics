###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = r'C:\Users\turni\Desktop\programowanie\prg-basics\prg-basics\08-FileHandling\Zadania\seven_wonders.txt'

# Sort data alphabetically
seven_wonders = sorted(seven_wonders)

# Write data to the file
def f(file_name):
   with open(file_name, 'w') as f:
      for item in seven_wonders:
        f.write(f"{item}\n")

f(file_name)