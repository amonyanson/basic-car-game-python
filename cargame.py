command = ""
started = False
stopped = False

while command != "quit":
    command = input(">: ")
    command = command.lower()
    if command == "start":
        if started:
            print("Car has already started")
        else:
            started = True
            print("Car has started")
    elif command == "stop":
        if stopped:
            print("Car has already stopped")
        else:
            stopped = True
            print("Car has stopped")
    elif command == "help":
        print("""
start - to start
stop - to stop
quit - to quit        
""")
    elif command == "quit":
        break
    else:
        print("I do not understand that")

