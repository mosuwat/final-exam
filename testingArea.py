from projectClasses import Customer, Driver

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