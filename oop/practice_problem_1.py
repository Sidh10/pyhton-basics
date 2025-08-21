class Car :
    def __init__(self,brand,model) :
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"I like to drive {self.brand} {self.model}"
        
    def info(self):
        print(f"I like cars of {self.brand} and the best one is {self.model}")

p1 = Car("Audi","A7")    
p1.info()   
