import json

def load_products():
    with open('Products.json') as f:
        products = json.load(f)
    return products
product_list = load_products()
print(product_list)


def save_products(products):
    with open('Products.json', 'w') as f:
        json.dump(products, f, indent=4)
    print('Saved successfully!')
save_products(product_list)


def view_products(products):
    for product in products:
        print(f'''
Name: {product['name']}
Price: {product['price']}
Quantity: {product['quantity']}
''')
view_products(product_list)