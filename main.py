class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(self, name)
        self.address = address

    def place_order(self, item):
        return DeliveryOrder(self.name, item, "preparing")

class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(self, name)
        self.vehicle = vehicle
    
    def deliver(self, order):
        order.status = "delivered"
        print(f"{self.driver_name} is delivering {order.item} to {order.name} using {self.vehicle}.")

class DeliveryOrder:
    def __init__(self, customer, item, status):
        self.cutomer = customer
        self.item = item
        self.status = status
    
    def assign_driver(driver):
        pass
    
    def summary():
        pass
