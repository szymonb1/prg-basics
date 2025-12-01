def pets_read():
    with open(r"prg-basics\08-FileHandling\pets.txt", 'r') as f:
        content = f.read()
    return content


file_words = pets_read().split()
print(len(file_words))


