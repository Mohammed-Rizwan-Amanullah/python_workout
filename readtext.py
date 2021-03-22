# f is variable defined to open file scores.txt
#we use "r" to read file
# we use "w" to write file
# we have created a file scores.txt using the python program writetext.py
# we are using that text file to create dictionary in this python script

f = open("scores.txt", "r")
participants = {}

for line in f:
    entry = line.strip().split(",") # .split will create a list and .strip will remove the extraline
    participant = entry[0]
    score = entry[1]
    participants[participant] = score
    print(participant + "  " + score)

f.close
print (participants)
