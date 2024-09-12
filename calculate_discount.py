def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    
    Returns:
    float: The final price after applying the discount if the discount is 20% or more,
           otherwise returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    
    final_price = calculate_discount(original_price, discount_percent)
    
    
    print(f"The final price is: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
