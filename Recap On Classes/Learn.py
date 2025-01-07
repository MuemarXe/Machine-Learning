#modules in python 
def making_pizza(size,*toppings):
    print("\nMaking a "+ str(size)+"-inch pizza with toppings ")
    for topping in toppings:
        print("-"+topping)

class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def sit(self):
        print(self.name.title()+ " is now sitting")
    def roll_over(self):
        print(self.name.title() +" is now rolling over")

myDog = Dog('Smith',20)
print("my dog's name is "+ myDog.name + " and age is  "+ str(myDog.age))
myDog.sit()
myDog.roll_over()
class Car():
    def __init__(self,name,make,year,torque):
        self.name =name
        self.make =make
        self.year =year
        self.torque =torque
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = self.name +' '+ self.make +'  '+ str(self.year)+' ' +str(self.torque)
        return long_name.title()
    def read_odometer(self):        
        print("This car has "+ str(self.odometer_reading) + " miles on it")

    def update_odometer(self,milage):
        if milage>= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_new_car = Car('Audi','A5', 2024,450)
my_new_car2 = Car('BMW','M5',2024,700)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
print(my_new_car2.get_descriptive_name())
#my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Inheritance
class ElectricCar(Car):
    def __init__(self,name,make,year,torque):
        super().__init__(name,make,year,torque)
        self.battery =Battery()
    
class Battery():
    def __init__(self,battery_size =70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a "+ str(self.battery_size) + "-kWh battery")

my_tesla =ElectricCar('Tesla','CyberTruck',2022,1000)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()