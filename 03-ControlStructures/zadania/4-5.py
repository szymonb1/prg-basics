import string

plain_text = 'The early bird catches the worm'
encrypted_text = ''



for char in plain_text:
    if ord(char) + 1 == 33:
        print(" ", end="")
    else:
        ascii_number = ord(char) + 1
        letter = chr(ascii_number)
        print(letter,end ='')

    # read the character's code (use ord())
    ...
    # add one to the character's code
    ...
    # replace new character code with its
    # corresponding character (use chr())
    ...
    # add encrypted character to encrypted text
    ...