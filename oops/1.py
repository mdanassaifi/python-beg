class car:
    total_car = 0
   
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"


    def  full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_description():
        return "This is a car class that represents different types of cars."


class ElectricCar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

# my_tesla = ElectricCar("tesla", "model s", "85 kWh")
# print(my_tesla.__brand)
# print(my_tesla.get_brand())

# print(my_tesla.fuel_type())


safari = car("tata", "safari")
safarithree = car("tata", "nexon")
print(safari.fuel_type())
print(safari.total_car)

print(car.general_description())
# my_car = car("suzuki", "shift")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


class Battery:
    def battery_info(self):
        return "Battery is a device that stores energy"

class engine:
    def engine_info(self):
        return "Engine is a machine that converts energy into mechanical power"

class elerctriccarTwo(Battery, engine, car):
    pass

my_new_tesla = elerctriccarTwo("tesla", "model ww", "85 kWh")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())