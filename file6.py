file_name = 'alice.txt'

try:
    with open(file_name) as f:
        alice_content = f.read()
except FileNotFoundError:
    print("File not present. Check the file location once again")
else:
    no_of_and = int(alice_content.lower().count('and'))
    print(f"the number of 'and' present in the file is {no_of_and} ")
