def Email():

    print("---------WELCOME TO EMAIL SLICER---------")
    print("Here you can know your username and entered domain ")
    email = input("Enter your email: ").strip()
    if "@" in email:
        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:]

        print(f"Your username is {username} & domain is {domain}")
    else:
        print("Please enter correct email ")


while True:
    Email()
    if input("Should I stop? ") == "yes":
        break
