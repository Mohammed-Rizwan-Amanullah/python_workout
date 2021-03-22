#exercise 2
def show_message(messages, final_messages):
    while messages:
        element = messages.pop()
        final_messages.append(element)


messages = ["mirzapur is the best web series", "family man is second best series", "sacred games is not up to the mark"]
final_messages = []
show_message(messages, final_messages)
print(messages)
print(final_messages)

#exercise 3
def show_message(messages, final_messages):
    while messages:
        element = messages.pop()
        final_messages.append(element)


messages = ["mirzapur is the best web series", "family man is second best series", "sacred games is not up to the mark"]
final_messages = []
show_message(messages[:], final_messages)
print(messages)
print(final_messages)

