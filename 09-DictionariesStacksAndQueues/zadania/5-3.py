translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

eng = input("Podaj slowo: ")
try:
    print(translations[eng])
except:
    print(":(")