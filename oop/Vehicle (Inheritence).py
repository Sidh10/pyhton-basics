class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def start_engine(self):
        print("Engine Started")
    def display_info(self):
        print(f"Car brand: {self.brand}")    
        print(f"Car model : {self.model}")
        print(f"Year of manufacturing : {self.year}")   
class Car(Vehicle):
    def __init__(self,brand,model,year,seat,fuel_type):
        super().__init__(brand,model,year)
        self.seat = seat
        self.fuel_type = fuel_type
    
    
    def display_info(self) :
        print(f"Car brand: {self.brand}")    
        print(f"Car model : {self.model}")
        print(f"Year of manufacturing : {self.year}")
        print(f"Seat type :{self.seat}")
        print(f"Fuel Type : {self.fuel_type}")
    def drive(self):
        print("Car is now driving")

class ElectricCar(Car):
    def __init__(self,brand,model,year,seat,fuel_type,battery_capacity):
        super().__init__(brand,model,year,seat,fuel_type)
        self.battery_capacity = battery_capacity
    def display_info(self):
         super().display_info()
         print(f"battery_capacity :{self.battery_capacity}")  
    def charge(self):
        print("Charging Battery")       

c1 = ElectricCar('Tesla','Model S',2024,5,'Electric','100 kWh')
c1.display_info()
