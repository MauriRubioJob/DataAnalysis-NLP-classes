keep_running = True

while keep_running:
    name = input("Enter your username: ")
    if len(name) >= 3:
        print("Welcome!")
        keep_running = False
    else:
        print("Name too short!")


print("You entered a valid name! Program terminated")