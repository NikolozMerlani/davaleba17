while True:
    command = input("> ")
    command = command.lower()
    if command == "start":
        if started == False:
            print("lesgo")
            started = True
        else:
            print("already started")
    elif command == "stop":
        if started == True:
            print("stopped")
            started = False
        else:
            print("already stopped")
    elif command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("help - helpdesk")
        print("quit - quit the game")


    elif command == "quit":
        print("bye")
        break
    else:
        print("weird input")
    