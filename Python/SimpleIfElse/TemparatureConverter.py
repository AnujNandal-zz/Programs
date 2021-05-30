print("Please select an option :")
print("\t 1. Convert temperature from celsius to fahrenheit")
print("\t 2. Convert temperature from fahrenheit to celsius")
option = (int(input()))
output = 0
if option == 1:
    C2F = (int(input("Enter the temperature you want to convert :\t")))
    output = (C2F*9/5)+32
    print(output)

if option == 2:
    F2C = (int(input("Enter the temperature you want to convert :\t")))
    output = (F2C-32)*5/9
    print(output)
