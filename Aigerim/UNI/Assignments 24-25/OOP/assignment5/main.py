from device import Device
from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet
from cart import Cart


if __name__ == '__main__':

    smartphone1 = Smartphone('Iphone X', 120000, 5, 12, 5, 100)
    smartphone2 = Smartphone('Iphone 11', 130000, 10, 12, 5.5, 100)
    smartphone3 = Smartphone('Iphone 12', 140000, 4, 12, 5, 100)
    smartphone4 = Smartphone('Iphone 13', 150000, 8, 12, 6, 100)
    smartphone5 = Smartphone('Iphone 14', 160000, 7, 12, 6, 100)
    smartphone6 = Smartphone('Iphone 15', 170000, 9, 12, 6.5, 100)
    smartphone7 = Smartphone('Iphone 16', 180000, 12, 12, 7, 100)
    Smartphone.smartphones.extend([smartphone1, smartphone2, smartphone3, smartphone4, smartphone5, smartphone6, smartphone7])

    laptop1 = Laptop('Asus', 80000, 8, 12, 16, 2.4)
    laptop2 = Laptop('Lenovo', 50000, 12, 12, 8, 2.0)
    laptop3 = Laptop('HP', 120000, 9, 12, 32, 4.8)
    laptop4 = Laptop('ThinkPad', 100000, 7, 12, 16, 2.4)
    laptop5 = Laptop('MacBook', 200000, 10, 12, 32, 4.8)
    laptop6 = Laptop('Macbook Air', 180000, 4, 12, 16, 2.4)
    laptop7 = Laptop('Asus Pro', 90000, 9, 12, 32, 2.4)
    Laptop.laptops.extend([laptop1, laptop2, laptop3, laptop4, laptop5, laptop6, laptop7])

    tablet1 = Tablet('Samsung Galaxy 1', 30000, 6, 12, '768×1024', 0.5)
    tablet2 = Tablet('Samsung Galaxy 2', 35000, 8, 12, '768×1024', 0.6)
    tablet3 = Tablet('Samsung Galaxy 3', 40000, 10, 12, '810×1080', 0.5)
    tablet4 = Tablet('Samsung Galaxy 4', 50000, 7, 12, '1280×800', 0.4)
    tablet5 = Tablet('IPad', 90000, 8, 12, '1024×768', 0.4)
    tablet6 = Tablet('IPad Pro', 120000, 9, 12, '1920×1080', 0.3)
    Tablet.tablets.extend([tablet1, tablet2, tablet3, tablet4, tablet5, tablet6])

    Device.devices.extend([Smartphone.smartphones, Laptop.laptops, Tablet.tablets])
    Device.devices = sum(Device.devices, [])

    def user_menu():
        print('Hello! Welcome to the DeviceStore!')

        while True:
            print('The numbers shown below for actions:')
            print('1 - Show Devices, \n2 - Show Cart, \n3 - Exit.')
            action = int(input('\nEnter number for actions: '))

            if action == 1:
                count = 0
                for smartphone in Smartphone.smartphones:
                    print(count + 1, '.')
                    count += 1
                    print(smartphone.display_info())
                for laptop in Laptop.laptops:
                    print(count + 1, '.')
                    count += 1
                    print(laptop.display_info())
                for tablet in Tablet.tablets:
                    print(count + 1, '.')
                    count += 1
                    print(tablet.display_info())

                choose = int(input('Would you like to choose device? (1-Yes, 0-No) '))
                while choose == 1:
                    choose_device = int(input('Enter the device number: '))
                    choose_amount = int(input('Enter the amount of device: '))
                    if 1 <= choose_device <= 7:
                        Cart.add_device(Smartphone.smartphones[choose_device - 1], choose_amount)
                    elif 8 <= choose_device <= 14:
                        Cart.add_device(Laptop.laptops[choose_device - 8], choose_amount)
                    elif 15 <= choose_device <= 20:
                        Cart.add_device(Tablet.tablets[choose_device - 15], choose_amount)
                    else:
                        return 'No such device number.'

                    choose = int(input('Would you like to choose device? (1-Yes, 0-No) '))
            elif action == 2:
                print('Your Cart:')
                Cart.print_items()
                checkout_check = int(input('Do you want a checkout? (1-Yes, 0-No) '))
                if checkout_check == 1:
                    Cart.checkout()
                    print('Thank you for shopping! ')
                    break
                else:
                    print('Thank you for shopping! ')
                    break
            else:
                print('You are exiting...')
                break


    user_menu()
