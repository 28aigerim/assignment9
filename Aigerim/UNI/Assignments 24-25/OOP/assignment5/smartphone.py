from device import Device


class Smartphone(Device):

    smartphones = []

    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def display_info(self):
        return (f'Device {self.name} with price {self.price}, '
                f'stock: {self.stock}, warranty period: {self.warranty_period} months.'
                f'Smartphone with screen size: {self.screen_size} and battery life: {self.battery_life}.')

    def __str__(self):
        return f'Smartphone with screen size: {self.screen_size} and battery life: {self.battery_life}.'

    def make_call(self):
        return 'You are making a call.'

    def install_app(self):
        return 'You are installing app.'