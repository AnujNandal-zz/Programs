# ----------------Break------------------------
print("Example of break:\n")
for letter in 'Python':
    if letter == 'h':
        break
    print('Current Letter :\t', letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        break
    print('Current variable value :\t', var)

# ---------------Continue----------------------
print("\nExample of continue:\n")
for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter :\t', letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Current variable value :\t', var)

# ------------------Pass-------------------------
print("\nExample of pass:\n")
for letter in 'Python':
    if letter == 'h':
        pass
    print('Current Letter :\t', letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        pass
    print('Current variable value :\t', var)
