color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open("file.txt", "w") as myfile:
    for c in color:
        myfile.write("%s\n" % c)

content = open('file.txt')
print(content.read())
