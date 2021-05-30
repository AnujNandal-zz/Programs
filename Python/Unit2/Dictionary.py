emp = {'Name': 'Anuj', 'Age': 18, 'Gender': 'Male'}
print(type(emp))
print(emp)
jtp = dict({1: 'Java', 2: 'T', 3: 'Point'})
print(jtp)
dt = dict([{1, 'Ashish'}, {2, 'Singh'}, {3, 'Rohila'}])
print(dt, '\n')

print("emp['Name']: ", emp['Name'])
print("emp['Age']: ", emp['Age'])
print("emp['Gender']: ", emp['Gender'])

print("\nName : %s" % emp['Name'])
print("Age : %d" % emp['Age'])
print("Gender : %s" % emp['Gender'])

emp['Age'] = 21
emp['College'] = 'JIMS VK-II'
print('\n', emp)

(emp['Name']) = input("Enter your Name: ")
(emp['Age']) = input("Enter your Age: ")
(emp['Gender']) = input("Enter your Gender: ")
(emp['College']) = input("Enter your College: ")
print(emp)

emp.pop('College')
print(emp)

emp.clear()
print(emp)
