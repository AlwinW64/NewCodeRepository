def CarGame():
    print("Car Game")
    command = input("> ")
    Car = 'Off'
    while command != 'end':
        if (command == 'start') and (Car == 'Off'):
            print("car started")
            Car = 'On'
        elif (command == 'start') and (Car == 'On'):
            print("Car already On")
        elif (command == 'stop') and (Car == 'On'):
            print("car stopped")
            Car = 'Off'
        elif (command == 'stop') and (Car == 'Off'):
            print("Car is already Off")
        elif command == 'help':
            print("help is on the way")
        else:
            print("Invalid Command")
        command = input("command: ")
    else:
        print("Game Over")
CarGame()