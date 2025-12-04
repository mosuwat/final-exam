class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item):
        return DeliveryOrder(Customer(self.name, self.address), item, "preparing")

class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    
    def deliver(self, order):
        if order.driver.name != self.name:
            print("This isn't their order!")
        else:
            order.status = "delivered"
            print(f"{self.name} is delivering {order.item} to {order.customer.name} using {self.vehicle}.")

class DeliveryOrder:
    def __init__(self, customer, item, status = "preparing"):
        self.customer = customer
        self.item = item
        self.status = status
        self.driver = None
    
    def assign_driver(self, driver):
        self.driver = driver
    
    def summary(self):
        print("Order Summary:")
        print(f"Item: {self.item}")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.status}")
        if self.driver == None:
            print(f"Driver: Not assigned")
        else:
            print(f"Driver: {self.driver.name}")