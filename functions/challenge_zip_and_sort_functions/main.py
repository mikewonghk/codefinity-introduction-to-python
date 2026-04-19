# List of product names
product_name = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

combined_list = list(zip(product_name, prices, quantities_sold))

sorted_products = sorted(combined_list)

for product_name, prices, quantities_sold in sorted_products:
    print(f"Product: {product_name}, Price: {prices}, Quantity Sold: {quantities_sold}")