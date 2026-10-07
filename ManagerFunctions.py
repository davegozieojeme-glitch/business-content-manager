import json

# Used to validate numeric input
def get_positive_number(prompt):
    while True:
        try:
            number = int(input(f'{prompt}'))
            if number <= 0:
                print('lesser than or equivalent to zero, number rejected!')
                continue
            break
        except ValueError:
            print('not a digit, number rejected!')
    return number


# Used to get products from Products.json file
def load_products():
    with open("Products.json", "r") as f:
        products = json.load(f)
    return products


# Used to save to Products.json file
def save_products(products):
    with open('Products.json', 'w') as f:
        json.dump(products, f, indent=4)
    print('Saved successfully!')


# Used to display saved products
def view_products(products):
    for product in products:
        print(f'''
Name: {product['name']}
Price: {product['price']}
Quantity: {product['quantity']}
''')


# Used to add a new product
def add_new_product():
    product_list = load_products()
    number_of_times = int(input('How many products do you want to add? '))
    for i in range(number_of_times):
        print(f'Product {i + 1}')
        p_name = input('Enter product name here: ')
        p_price = get_positive_number('Enter product price here: ')
        p_quantity = get_positive_number('Enter product quantity here: ')
        print('-------------------------------------------------------------------')

        product = {
            'name': p_name,
            'price': p_price,
            'quantity': p_quantity
        }
        product_list.append(product)

    save_products(product_list)


# To search for a product
def search_products():
    product_list = load_products()
    search = input('Enter product name to search: ')
    present = False
    for product in product_list:
        if search.upper() == product['name'].upper():
            present = True
            print('Product found!')
    if not present:
        print('Product not found!')


# To delete a product from list
def delete_product():
    product_list = load_products()
    search = input('Enter product name to delete: ')
    present = False
    for index, product in enumerate(product_list):
            if search.upper() == product['name'].upper():
                present = True
                product_list.pop(index)
                print('Product deleted!')
                break
    if not present:
        print('Product not found!')
    print(product_list)
    save_products(product_list)


# To update the price of a product from list
def update_product_price():
    product_list = load_products()
    search = input('Enter product name to update price: ')
    present = False
    for product in product_list:
            if search.upper() == product['name'].upper():
                present = True
                product['price'] = get_positive_number('Enter product price here($): ')
                print('Product updated! Check Products.json to confirm!')
                break
    if not present:
        print('Product not found!')
    print(product_list)
    save_products(product_list)