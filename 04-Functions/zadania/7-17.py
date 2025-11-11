def f(sentence):
    backwards_sentence = ""
    for x in range(len(sentence), 0, -1):
        backwards_sentence += sentence[x-1]
    if sentence == backwards_sentence:
        print(sentence, "to palindrome")
    else:
        print(sentence, "to nie palindrome")
def main():
    f("niggin")
if __name__ == "__main__":
    main()

