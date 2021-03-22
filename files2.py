file_name = 'inpython.txt'

#1 reading entire file
with open(file_name) as file_object:
    lines = file_object.read()
print(lines.strip() + "\n")

#2 loopin gover file object
with open(file_name) as file_object2:
    for line in file_object2:
        print(line.rstrip())

print("\n")

#3 storing lines in a list
with open(file_name) as file_object3:
    lines = file_object3.readlines()

for line in lines:
    print(line.strip())

print("\n")

new_line = ''
for line in lines:
    print(line.replace('python', 'R').strip())
    new_line += line.replace('In', 'Out') #replace and assign to new variable

print(new_line)
