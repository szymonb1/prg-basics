
attempts = 0
pin = "0805"
while attempts<3:
    entered_pin = str(input("Enter the PIN code: "))
    if pin == entered_pin:
        print("git")
        break
    else:
        attempts += 1
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")
    