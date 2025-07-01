# Industry Example: Process Orders with Loop Control

orders = [101, 102, None, 104, 105]

for order in orders:
    if order is None:
        print("Missing order, skipping...")
        continue  # skip None orders
    if order == 105:
        print("Reached final order, stopping process.")
        break  # stop at last order
    print(f"Processing order {order}")
else:
    print("All orders processed successfully.")
