f = open("scores.txt", "w")
while True:
    participant = input("participant name >")

    if participant == "quit":
        print("quitting...")
        break;
    score = input("enter the score for participant")

    f.write(participant + ", " + score + "\n")

f.close()
