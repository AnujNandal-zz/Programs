str1 = "Jagannath Institute of Management Sciences"
str2 = str1.upper()
str3 = " "
str4 = "II"
str5 = "    Jagannath Institute of Management Sciences    "

# Boolean Methods
print("Check whether string is alphanumeric", str1.isalpha())

print("Check whether string is digit", str1.isdigit())

print("Check whether string is title", str1.istitle())

print("Check whether string is space", str3.isspace())

print("Check whether string is uppercase", str2.isupper())

print("Check whether string is lowercase", str1.islower())

# Join, Spilt Methods
print("Joining the strings: ", str1.join(str4))

print("Joining the strings: ", " ".join(reversed(str1)))

print("Spilting the strings: ", str1.split("i"))

print("Replacing the strings: ", str1.replace("Sciences", "School"))

# Strip, Len Methods
print("The total characters in a string", len(str1))

print("Striping the spaces in strings: ", str5.lstrip())

print("Striping the spaces in strings: ", str5.rstrip())

print("The total charcaters in a string after lstrip: ", len(str5.lstrip()))

print("The total charcaters in a string after rstrip: ", len(str5.rstrip()))

# Partition, Find and Count Methods
print("Partition of a string: ", str1.partition("of"))

print("Finding a character in a string: ", str5.find("M"))

print("Finding a character in a string: ", str5.rfind("M"))

print("The count of a character in a string: ", str1.count("e"))

# Startswith function
st = "Hello World"
st2 = st.startswith("World", 6, 11)
print(st2)
