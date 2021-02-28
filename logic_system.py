"""
This module deals with class of logistic systems.
"""
from random import randint

class Item:
    """
    Class for items representation(name and price).
    """
    def __init__(self, name: str, price: float):
        """
        Creates an item which will be ordered.
        >>> my_item = Item('book', 110)
        >>> my_item.name
        'book'
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        Returns a string to represent the item.
        >>> my_item = Item('book', 110)
        >>> print(my_item)
        Item('book',110)
        """
        return f'Item(\'{self.name}\',{self.price})'

class Location:
    """
    Class for locations representation(city and postoffice).
    """
    def __init__(self, city: str, postoffice: int):
        """
        Creates a location to which the order will be transfered.
        >>> my_location = Location('Lviv', 53)
        >>> my_location.postoffice
        53
        """
        self.city = city
        self.postoffice = postoffice

class Vehicle:
    """
    Class for vehicles representation(number and accessibility).
    """
    def __init__(self, vehicleNo: int):
        """
        Creates a vehicle on which an order will be transfered.
        >>> vehicle = Vehicle(1)
        >>> vehicle.vehicleNo
        1
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = True

class Order:
    """
    Class for orders representation(ID, username, location, items and vehicle).
    """
    def __init__(self, user_name: str, city, postoffice, items):
        '''
        Creates a full order off an object.
        '''
        self.orderId = randint(100000000, 999999999)
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None

    def __str__(self):
        """
        Returns a string to represent the item.
        """
        return f'Your order number is {self.orderId}'

    def calculateAmount(self):
        """
        Calculates the total summary of the items.
        """
        total_sum = 0
        total_sum = sum(item.price for item in self.items)
        return total_sum

    def assignVehicle(self, vehicle: Vehicle):
        '''
        Assigns a vehicle for an order.
        '''
        if vehicle.isAvailable == True:
            self.vehicle = vehicle
            vehicle.isAvailable = False

class LogisticSystem:
    """
    Class for orders manipulation.
    """
    def __init__(self, vehicles):
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        """
        Function places an order if a vehicle is available.
        """
        for vehicle in self.vehicles:
            if vehicle.isAvailable == True:
                self.orders.append(order)
                vehicle.isAvailable = False
                break
            else:
                return 'There is no available vehicle to deliver an order.'

    def trackOrder(self, orderId: int):
        """
        Tracks order if it exists, else return "No such order".
        """
        for order in self.orders:
            if orderId == order.orderId:
                return f'Your order #{orderId} is sent to {order.location.city}.\
 Total price: {order.calculateAmount()} UAH.'
            else:
                return "No such order"

import doctest
doctest.testmod()