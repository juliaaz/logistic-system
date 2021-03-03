import sys
from logic_system import Item, Vehicle, Order, Location, LogisticSystem

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.logic_system = LogisticSystem(vehicles=[])
        self.items = []
        self.choices = {
                "1": self.add_vehicle,
                "2": self.add_item,
                "3": self.complete_order,
                "4": self.trackOrder,
                "5": self.quit
}

    def display_menu(self):
        """
        Shows the options of the menu.
        """
        print("""
Logistic System Menu
1. Add Vehicles
2. Add Item To The Cart
3. Complete The Order
4. Track The Order
5. Quit """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            option = input('Input one of the option:')
            action = self.choices.get(option)
            if action:
                action()
            else:
                print(f'{option} is an invalid option.')
    
    def add_vehicle(self):
        vehicle_No = int(input('Enter the number of the vehicle: '))
        vehicle = Vehicle(vehicle_No)
        self.logic_system.vehicles.append(vehicle)
    
    def add_item(self):
        item_name = input('Input the name of the item: ')
        try:
            item_price = float(input(f'Input the price of the {item_name}: '))
            item = Item(item_name, item_price)
            self.items.append(item)
        except ValueError:
            print('Oops. Try again :-)')


    def complete_order(self):
        user_name = input('Input your name: ')
        city = input('Input your city: ')
        postoffice = input('Input postoffice to deliver: ')
        order = Order(user_name, city, postoffice, self.items)
        self.items = []
        print(order)
        if isinstance(self.logic_system.placeOrder(order), str):
            print(self.logic_system.placeOrder(order))
        self.logic_system.placeOrder(order)

    def trackOrder(self):
        flag = input('Do you want to check all the orders? Type "All" if it" True: ')
        if flag == 'All':
            for order in self.logic_system.orders:
                print(self.logic_system.trackOrder(order.orderId))
        else:
            try:
                orderId = int(input('In order to check the order, \
please, input the id of the order you want to track: '))
            except ValueError:
                print('Oops. Try again :-)')
            print(self.logic_system.trackOrder(orderId))

    def quit(self):
        print("Thank you for using the logistic system. Have a good day!")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()