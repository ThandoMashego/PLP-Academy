def calculate_discount(price, discount_percent):
    if discount_percent >= 20 :
        discount = price * discount_percent/100.    # Apply discount if 20% or more
        return price - discount                     # Subtract the discount from the price
    else:
        return price                                # Return the original price if discount < 20%

price_item = int(input("please enter the price of the item  "))
discount_item = int(input("Please enter the discount percent of the item ?"))
final_price = calculate_discount(price_item,discount_item)
print(f"The final price after applying the discount is: {final_price}")
