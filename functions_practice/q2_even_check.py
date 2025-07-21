a = int(input("Enter your Number"))
def fun(a) :
    if a%2 == 0 :
       print("even")
    else :
       print("odd")
fun(a)

better version 
a = int(input("Enter your Number"))

def fun(a):
    if a % 2 == 0:
        return "even"
    else:
        return "odd"

result = fun(a)
print(result)
