from itertools import product

from ManagerFunctions import *

print('''
This is the business content manager.
Using your keypad, press * to continue.
''')

unlocked = False

while True:
    command = input('> ')
    match command:
        case '*':
            unlocked = True
            print('Keypad unlocked!')

            print('''
To perform tasks, press:
1 => view available products
2 => search through the products
3 => update product price
4 => create new product
5 => delete product

''')

        case '1':
            view_products(product)

        case '2':
            search_products()

        case '3':
            update_product_price()

        case '4':
            add_new_product()

        case '5':
            delete_product()