# SmartBuy Supermarket Billing System

print("WELCOME TO SMARTBUY SUPERMARKET")

continue_program = "Y"

while continue_program.upper() == "Y":

    # Lists to store product information
    product_names = []
    quantities = []
    prices = []
    totals = []

    grand_total = 0

    # Input number of products
    num_products = int(input("\nEnter number of products: "))

    # Collect product details
    for i in range(num_products):
        print(f"\nProduct {i + 1}")

        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter unit price: "))

        total = quantity * price

        product_names.append(name)
        quantities.append(quantity)
        prices.append(price)
        totals.append(total)

        grand_total += total

    # Discount calculation
    if grand_total > 500:
        discount = grand_total * 0.10
    else:
        discount = 0

    amount_due = grand_total - discount

    # Receipt
    print("\n")
    print("=" * 50)
    print("       SMARTBUY SUPERMARKET RECEIPT")
    print("=" * 50)

    print(f"{'Product':18}{'Qty':>8}{'Price':>10}{'Total':>10}")

    for i in range(len(product_names)):
        print(f"{product_names[i]:18}{quantities[i]:>8}{prices[i]:>10.2f}{totals[i]:>10.2f}")

    print("-" * 50)
    print(f"Subtotal:      Le {grand_total:.2f}")
    print(f"Discount:      Le {discount:.2f}")
    print(f"Amount Due:    Le {amount_due:.2f}")
    print("=" * 50)

    # Process next customer
    continue_program = input("\nProcess another customer? (Y/N): ")

print("\nThank you for using SmartBuy Supermarket Billing System!")