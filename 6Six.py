from Signature.signature import sign
#WRite python code to demonstrate input
print("WE take input and print ")

def takeInput():
    name = input("Please enter your name here ")

    age = int(input("Please enter your age "))

    print(name, " ", age)

takeInput()
sign("Yash", "015")
