menu = '''
Start - To start the car
Stop - To stop the car
Quit - To exit

'''

unknown = "I don't understand that..."
start = "Car Started...Ready to go!"
stop = "Car Stopped."

i = 0
while i == 0:
    command = input(">")
    if command.upper() == "START":
        print(start)
    elif command.upper() == "HELP":
        print(menu)
    elif command.upper() == "STOP":
        print(stop)
    elif command.upper() == "QUIT":
        break
    else:
        print(unknown)

