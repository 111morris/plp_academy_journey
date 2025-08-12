def calculate_discount(price, discount_percent):
 if discount_percent >= 20:
  discount_amount = (discount_percent/100) * price
  final_price = price - discount_amount
  return final_price
 else: 
  return price


try: 
 original_price = float(input("Enter the original price of the item: " ))
 discount = float(input("Enter the discount percentage: "))

 final_price = calculate_discount(original_price, discount)


 if discount >= 20: 
  print(f"Discount applied. Final: price: ${final_price}")
 else: 
  print(f"No discount applied. Final price: ${original_price}")
except ValueError: 
 print("Enter a valid number")