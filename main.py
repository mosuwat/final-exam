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
        self.driver = ''
    
    def assign_driver(self, driver):
        self.driver = driver
    
    def summary(self):
        print("Order Summary:")
        print(f"Item: {self.item}")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.status}")
        print(f"Driver: {self.driver.name}")

customer1 = Customer("Alice", "123")
customer2 = Customer("Bob", "456")
driver1 = Driver("David", "motorcycle")
customer1.introduce()
customer2.introduce()
driver1.introduce()
print()

order1 = customer1.place_order("Laptop")
order1.assign_driver(driver1)
order1.summary()
print()

order2 = customer2.place_order("Headphones")
order2.assign_driver(driver1)
order2.summary()
print()

driver1.deliver(order1)
driver1.deliver(order2)
print()

print("Final Status:")
print(f"Order for Laptop → {order1.status}")
print(f"Order for Headphones → {order2.status}")