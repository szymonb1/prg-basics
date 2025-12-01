file_path = str(input("Podaj nazwe pliku: "))

try:
    with open(r"prg-basics\08-FileHandling\Zadania\\"+file_path, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("zly plik misiek")


words = content.split()
lines = content.splitlines()
words_amount = len(words)
lines_amount = len(lines)
characters_amount= 0
for word in words:
    for x in word:
        characters_amount+=1


print(f"File name: {file_path}")
print(f"Number of lines: {lines_amount}")
print(f"Number of words: {words_amount}")
print(f"Number of characters: {characters_amount}")


