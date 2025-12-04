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
    def __init__(self, customer, item, status = "preparing"):
        self.cutomer = customer
        self.item = item
        self.status = status
        self.driver = ''
    
    def assign_driver(self, driver):
        self.driver = driver
    
    def summary(self):
        print("Order Summary:")
        print(f"Item: {self.item}")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.status}")
        print(f"Driver: {self.driver.name}")
