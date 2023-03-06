command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car is starting...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car is stopping...")
    elif command == "quit":
        print("Quitting")
        break
    elif command == "help":
        print("""
Start -> Start the car
Stop -> Stop the car
Help -> Show this
        """)
    else:
        print("Invalid command")