def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.

    Returns:
        float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

def main():
    """"
    Main function to prompt user input and calculate the final price.
    """
    try:
        # Prompt the user for the original price
        original_price = float(input("Enter the original price of the item: "))

        # Prompt the user for the discount percentage
        discount_percentage_input = input("Enter the discount percentage (e.g., 20 or 20%): ").strip()

        # Remove the '%' symbol if present
        if discount_percentage_input.endswith('%'):
            discount_percentage_input = discount_percentage_input[:-1]

        # Convert the discount percentage to a float
        discount_percentage = float(discount_percentage_input)

        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percentage)

        # Print the result
        if discount_percentage >= 20:
            print(f"The final price after applying the discount is: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: ${original_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

# Run the main function
if __name__ == "__main__":
    main()