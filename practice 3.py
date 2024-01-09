#Create a Nested dictionary to store the item category, item name, item code, price, and stock. And display the list of items using thefunction.  
# Define a nested dictionary to store information about items

items = {
    'item1': {
        'category': 'Electronics',
        'name': 'Laptop',
        'code': 'LT001',
        'price': 1500.00,
        'stock': 50
    },
    'item2': {
        'category': 'Clothing',
        'name': 'T-shirt',
        'code': 'TS002',
        'price': 35.00,
        'stock': 100
    },
    'item3': {
        'category': 'Books',
        'name': 'Python Programming',
        'code': 'BK003',
        'price': 36.00,
        'stock': 30
    },
    'item4': {
        'category': 'Home Appliances',
        'name': 'Coffee Maker',
        'code': 'CA004',
        'price': 60.00,
        'stock': 20
    }
}

# Function to display the list of items
def display_items(item_dict):
    print("List of Items:")
    print("-" * 50)  # Line to separate the header
    
    # Iterate through each item in the dictionary
    for item_key, item_info in item_dict.items():
        print(f"Item Code: {item_info['code']}")
        print(f"Category: {item_info['category']}")
        print(f"Name: {item_info['name']}")
        print(f"Price: ${item_info['price']:.2f}")
        print(f"Stock: {item_info['stock']} units")
        print("-" * 50)  # Line to separate each item

# Call the function to display the list of items
display_items(items)