# Delivering Program (Final Exam)

## Project Overview
this project is a small delivery order placing program with assigning driver to each order and also completing them.

## Project Structure

### final-exam

- `READEME.md`: This readme file
- `testingArea.py`: The testing area for this project.
- `projectClasses.py`: Store all the classes.

## Feature

### Person Class

Located in `projectClasses.py` and used as the main parent class for the others, this class includes:

**Attributes**
- `name` (str): The name of the person.

**Methods**
- `introduce(self)`: saying the person name.

### Customer Class

Located in `projectClasses.py`, this class is inherited from the `Person` class and used to make a customer, the class include:

**Attributes**

- `name` (str): The customer name.
- `address` (str): The address of this person.

**Methods**

- `place_order(self, item)`: Place an order for the given `item`.

### Driver Class

Located in `projectClasses.py`, this class is inherited from the `Person` class and used to make a driver, the class include:

**Attributes**

- `name` (str): The driver name.
- `vehicle` (str): the driver's vehicle.

**Methods**

- `deliver(self, order)`: Check if the order matched their name, If `True` change the `order` status to be `delivered` and return a finishing `string`.

### DeliveryOrder Class

Located in `projectClasses.py`, this class is used to make and order, the class include:

**Attributes**

- `customer` (object): The customer.
- `item` (str): The order's item.
- `status` (str): Status of the delivery.
- `driver` (object): The order's driver.

**Methods**

- `assign_driver(self, driver)`: Assign the given `driver` to this `order`.
- `summary(self)`: show all the data of this order.

##  Running the Code

To run the data processing, execute `testingArea.py`:

```bash
python testingArea.py
