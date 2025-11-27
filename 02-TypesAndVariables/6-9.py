###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(f'Capitalized: {movie.upper()}')

# print title in small letters
print(f'Lower case: {movie.lower()}')

# print how many times the vowel "e" appears in the title
print(f'e appears {movie.count("e")} times')

# print where in the text is the word "Lord"

print(f'Tekst Lord na pozycji {movie.find("Lord")}')
# print where in the text is the word "dragon"
print(f'Tekst dragon na pozycji {movie.find("dragon")}')
# -1 czyli nie znaleziono