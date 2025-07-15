import random, time

alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y", "z", "q", "x", "t"]
numbers=[0,1,2,3,4,5,6,7,8,9]
specials=["!", "@", ".", ",", "#", "$", "%", "^", "/", "?", "<", ">"]
passpool=[]
password=''

print("Welcome to password generator.")

while True:
    try:
        length = int(input("Please enter the desired length of your password: "))
        break
    except ValueError:
        print("Please enter a valid number.")

bigwords = input("Do you want uppercase characters in your password? (y/n) ")
spec = input("Do you want to include special keywords in your password? (y/n) ")

for i in alphabet:
    passpool.append(i)
for i in numbers:
    passpool.append(i)

if bigwords == "y":
    for i in alphabet:
        passpool.append(i.upper())
if spec == "y":
    for i in specials:
        passpool.append(i)

for i in range(0, length):
    tmpsswd=str(random.choice(passpool))
    password=password + tmpsswd

print(password)
