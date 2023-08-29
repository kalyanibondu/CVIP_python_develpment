import random
upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters=upper_letters.lower()
digits="1234567890"
symbols="@#$%^&*()-={}:"
upper,lower,nums,syms=True,True,True,True
password=""
if upper:
    password+=upper_letters
if lower:
    password+=lower_letters
if nums:
    password+=digits
if syms:
    password+=symbols
amount=int(input("numbers of passwords: "))
len_password=int(input("enter the length: "))
for i in range(amount):
    a="".join(random.sample(password,len_password))
    print(f"your password is {a}")
