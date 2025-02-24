class Device:

    devices = []

    def __init__(self, name, price, stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
        return (f'Device {self.name} with price {self.price}, '
                f'stock: {self.stock}, warranty period: {self.warranty_period} months.')

    def __str__(self):
        return (f'Device {self.name} with price {self.price}, '
                f'stock: {self.stock}, warranty period: {self.warranty_period} months.')

    def apply_discount(self, discount_percentage):
        self.price = self.price / 100 * discount_percentage

    def is_available(self, amount):
        if self.stock >= amount:
            return True
        else:
            return False

    def reduce_stock(self, amount):
        self.stock -= amount