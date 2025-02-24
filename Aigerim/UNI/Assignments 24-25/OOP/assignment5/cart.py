from device import Device
from datetime import datetime


class Cart:

    items = []
    total_price = 0

    @classmethod
    def add_device(cls, device, amount):
        if device.is_available(amount):
            Cart.items.append((device.name, amount))
            Cart.total_price += device.price * amount
        else:
            return 'The amount is not available in the stock.'

    @classmethod
    def remove_device(cls, device, amount):
        for item in Cart.items:
            if item[0] == device:
                if item[1] == amount:
                    Cart.items.remove((device.name, amount))
                    Cart.total_price -= device.price * amount
                else:
                    item[1] -= amount
                    Cart.total_price -= device.price * amount

    @classmethod
    def get_total_price(cls):
        return f'The total price in the cart is {Cart.total_price} soms.'

    @classmethod
    def print_items(cls):
        if Cart.items != []:
            for item in Cart.items:
                print(item, end='\n')
        else:
            return 'The cart is empty.'

    @classmethod
    def checkout(cls):
        print('Check:')
        for item in Cart.items:
            for device in Device.devices:
                if item[0] == device.name:
                    print(f'Device {device.name}: {item[1]} --- {device.price * item[1]} som.')
                    device.reduce_stock(item[1])
        print(f'Total price: {Cart.total_price} som.')
        print(datetime.now())