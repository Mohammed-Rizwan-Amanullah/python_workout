guest = ["jones","martha","mads","nielson","tiderman"]
message = "I corially welcome you to my dark season"
print(guest[0].title() + " " + message)
print(guest[1].title() + " " + message)
print(guest[2].title() + " " + message)
print(guest[3].title() + " " + message)
print(guest[4].title() + " " + message)

guest_unavailable = guest.pop()
print (f"Unfortunately our guest {guest_unavailable.title()} cant make it to the party")
guest.append("adam")
print (guest)
guest.insert(0,"elisabeth")
print (guest)

print ("\nHappy to let you all know taht we have a bigger table now")
guest.insert(0,"eva")
guest.insert(2,"claudia")
guest.append("regina")
print(guest)

guest_popped = guest.pop()
print(f"i'm so sorry {guest_popped.title()} to remove you from the list")

guest_popped = guest.pop()
print(f"\ni'm so sorry {guest_popped.title()} to remove you from the list")

guest_popped = guest.pop()
print(f"\ni'm so sorry {guest_popped.title()} to remove you from the list")

guest_popped = guest.pop()
print(f"\ni'm so sorry {guest_popped.title()} to remove you from the list")
guest_popped = guest.pop()
print(f"\ni'm so sorry {guest_popped.title()} to remove you from the list")
guest_popped = guest.pop()
print(f"\ni'm so sorry {guest_popped.title()} to remove you from the list")
guest_popped = guest.pop()
print(f"\ni'm so sorry {guest_popped.title()} to remove you from the list")

print ("\n now we have only the below people in the list")
print(guest)

print("but i dont feel it is good to have those two people alone")
del guest[0]
del guest[0]

print("\n as mentioned i have removed all the people in the list")
print("see for yourself")
print(guest)
)
