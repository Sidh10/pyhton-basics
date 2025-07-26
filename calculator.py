x = int(input("Enter your number : "))
y = int(input("Enter your number : "))
def calc(x,y):
    operation = (input("Enter your operation(add/sub/mul/div) = "))
    match operation :
        case "add" : 
            return x + y
        case "sub" :
            return x - y
        case "mul" :
            return x*y
        case "div":
            if y != 0 :
                return x/y
            else: 
                return "not possible"
        case _:
            return " Not valid"
        
calculator = calc(x,y)
print(calculator)
