password = input("Enter password: ")

has_number = False
has_alphabet = False

for ch in password:
    if ch.isdigit():
        has_number = True

    if ch.isalpha():
        has_alphabet = True

if len(password) >= 8 and has_number and has_alphabet:
    print("Strong Password")
else:
    print("Weak Password")