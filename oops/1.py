class car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"


    def  full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"


class ElectricCar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("tesla", "model s", "85 kWh")
# print(my_tesla.__brand)
# print(my_tesla.get_brand())

print(my_tesla.fuel_type())


safari = car("tata", "safari")
print(safari.fuel_type())

# my_car = car("suzuki", "shift")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())