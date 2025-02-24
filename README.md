# Electronic Device Shopping Cart
----
##### Class called Device that defines common attributes and behaviors for all devices.
- Attributes:
name: The name of the device (e.g., "iPhone 13", "MacBook Pro").
price: The price of the device.
stock: The number of units available in the store.
warranty_period: The warranty period for the device in months.
- Methods:
__init__(self, name, price, stock, warranty)
display_info(self): Displays the basic details of the device (name, price, stock, warranty).
__str__(self): Displays the basic details of the device (name, price, stock, warranty).
apply_discount(self,discount_percentage): Reduces the price by a specified discount percentage.
is_available(self,amount): Checks if the device is available in the required quantity. Returns True if available, False otherwise.
reduce_stock(self,amount): Reduces the stock by the specified quantity when a purchase is made.
This class should serve as the foundation for all other types of devices.


##### Smartphone (Inherits from Device):
Attributes:
screen_size: The size of the screen in inches.
battery_life: The battery life in hours.
Methods:
__str__(self): String representation of Smartphone
make_call(self): Simulates making a call.
install_app(self): Simulates installing an app.
##### Laptop (Inherits from Device):
Attributes:
ram_size: The amount of RAM in GB.
processor_speed: The speed of the processor in GHz.
Methods:
__str__(self): String representation of Laptop
run_program(self): Simulates running a program on the laptop.
use_keyboard(self): Simulates typing on the keyboard.
##### Tablet (Inherits from Device):
Attributes:
screen_resolution: The screen resolution (e.g., "2048x1536").
weight: The weight of the tablet in grams.
Methods:
__str__(self): String representation of Tablet
browse_internet(self): Simulates browsing the internet.
use_touchscreen(self): Simulates using the touchscreen for navigation.


##### Cart Class:
Attributes:
items: A list of tuples, where each tuple contains a device and the amount being purchased.
total_price: The total price of all devices in the cart.
Methods:
add_device(self, device, amount): Adds a specified quantity of a device to the cart if it’s available in stock and updates the total_price.
remove_device(self, device, amount): Removes a specified quantity of a device from the cart and updates the total_price.
get_total_price(self): Retrieves the total price in the cart.
print_items(self): Prints all devices with their amounts in the cart.
checkout(self): Ensures all devices in the cart are available in the specified quantity. If they are, reduce the stock and print a receipt.


### Run the Application
Devices: Created 20 devices with varying names, prices, and stock quantities.
Show User Menu: Simple menu-driven application that presents the following options to the user:
#1 Show Devices: Display a list of all available devices with their details (name, price, stock, etc.).
#2 Show Cart: Display the current items in the user's shopping cart.
#3 Exit: Exit the program.
Show Devices: When the user selects option #1 (Show Devices), the system will display all the available devices with their details (name, price, stock, etc.). Each device in the list will have a corresponding option to allow the user to choose which device they want to add to the cart.
Show Cart: When the user selects option #2 (Show Cart), the system will display the devices that have been added to the cart along with their quantities and total price.
