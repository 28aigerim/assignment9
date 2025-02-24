from device import Device


class Laptop(Device):

    laptops = []

    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):

        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def display_info(self):
        return (f'Device {self.name} with price {self.price}, '
                f'stock: {self.stock}, warranty period: {self.warranty_period} months.'
                f'Laptop with RAM size: {self.ram_size} and processor speed: {self.processor_speed}.')

    def __str__(self):
        return f'Laptop with RAM size: {self.ram_size} and processor speed: {self.processor_speed}.'

    def run_program(self):
        return 'You are running a program.'

    def use_keyboard(self):
        return 'You are using a keyboard.'