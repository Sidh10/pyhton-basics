a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 
c = int(input("Enter third number: "))
if a > b :
    if a > c:
        print("Max is:", a)
    else:
        print("Max is:", c)
elif b > c:
    print("Max is:", b)

else:
    print("Max is:", c)
