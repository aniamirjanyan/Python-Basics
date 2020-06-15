message = "Hello World"

print(message)                  # prints the message
print(len(message))             # prints the length of the message
print(message[0])               # prints the first item
print(message[0:5])             # all char between 0 and 5 not included

print(message.lower())          # lower case
print(message.upper())          # upper case
print(message.count("Hello"))   # counts the number of "Hello"s
print(message.find("World"))    # the index which the word is at

new_message = message.replace("World", "Universe")      # replaces World with Universe

greeting = "Hello"
name = "Michael"
message = "{}, {}. Welcom!".format(greeting, name)      # placeholders
message = f"{greeting}, {name}. Welcome!"               # same thing
print(message)

print(dir(name))                # shows all methods we have access to with that variable
print(help(str))                # lot more information


