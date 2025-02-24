from device import Device


class Tablet(Device):

    tablets = []

    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):

        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
        return (f'Device {self.name} with price {self.price}, '
                f'stock: {self.stock}, warranty period: {self.warranty_period} months.'
                f'Tablet with screen resolution: {self.screen_resolution} and '
                f'weight: {self.weight} kg.')

    def __str__(self):
        return (f'Tablet with screen resolution: {self.screen_resolution} and '
                f'weight: {self.weight} kg.')

    def browse_internet(self):
        return 'You are browsing internet.'

    def use_touchscreen(self):
        return 'You are using touchscreen.'