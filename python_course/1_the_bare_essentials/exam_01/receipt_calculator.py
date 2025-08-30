
welcome_message = "--- Welcome to the Receipt Calculator ---"
print(welcome_message)


label = "--- YOUR RECEIPT ---"
separator = "--------------------"

product_name = input("Enter product name:")
product_name_formatted = product_name.upper()

product_quantity = int(input("Enter quantity:"))

product_price = float(input("Enter price per unit:"))
total_price = product_quantity * product_price



is_expensive = total_price > 100

print(label)
print(f"Product: {product_name_formatted}")
print(f"Quantity: {product_quantity}")
print(f"Price: {product_price}")
print(separator)
print(f"TOTAL: {total_price}")
print(separator)
print(f"Expensive purchase check: {is_expensive}")

