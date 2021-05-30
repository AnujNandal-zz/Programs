price = 100
quantity = (int(input("Enter the quantity you purchased :\t")))
total = 0
if quantity > 1000:
    total = (quantity*price)*0.10
    print("Your total price is", total)
else:
    total = (price*quantity)
    print("Your total price is", total)
