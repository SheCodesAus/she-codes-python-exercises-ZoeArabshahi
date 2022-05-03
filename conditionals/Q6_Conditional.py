email=input("What is your email? ")

if email.find(".") and email.find("@"):
    print("Email is valid!")
else:
    print("Invalid!")
