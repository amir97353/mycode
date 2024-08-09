#!/usr/bin/python3

"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      secret
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    #print the players health
    print('Health:', health)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []
#The player will start with 3 health
health = 3

# a dictionary linking a room to other rooms
rooms = {
    'Library' : {
          'south' : 'Kitchen',
          'east'  : 'Hall',
          
        },
    'Hall' : {
          'south' : 'Kitchen',
          'east'  : 'Dining Room',
          'west'  : 'Library',
          'item'  : 'key'
          
        },

    'Kitchen' : {
          'north' : 'Hall',
          'item'  : 'monster',
        },
    'Dining Room' : {
          'west' : 'Hall',
          'south': 'Garden',
          'item' : 'potion'
       },
    'Garden' : {
          'north' : 'Dining Room'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')
    

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    move = move.lower().split(" ", 1)
    # Move starts off as a string but is coverted to a list wheb the .spliit method above is called on it
    # This splits the string into a list using a space (" ") as the delimiter.
    # The 1 argument specifies that the split should only happen once, producing a maximum of two elements in the list: the command and its argument.

    # Check if they type 'go' first
    if move[0] == 'go':
        # Ensure the user provided a direction
        if len(move) > 1 and move[1] in rooms[currentRoom]:
            # Set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')
    # The code checks if the direction is valid from the current room.
    # If valid, the player moves to the new room.
    # If invalid, it prints a message telling the player they can’t go that way.  

    if currentRoom == 'Library':
        print("You have found the book of infinite wisdom in the library. You now have infinite health")
        health = float('inf')
        inventory.append("Book of infinte wisom")
        print(inventory)

    # Check if they type 'get' first
    if move[0] == 'get':
        # Ensure the user provided an item to get
        if len(move) > 1 and "item" in rooms[currentRoom] and move[1] == rooms[currentRoom]['item']:
            # Add the item to their inventory
            inventory.append(move[1])
            print(move[1] + ' got!')
            # Delete the item from the room's dictionary
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')

    if move[0] == "secret":
        print("You have found a magic sword crafted in the forgotten lands")
        inventory.append("Forgotten blade")

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == 'monster':
        health -=1
        print("You were attacked by a monster you loose one health point")
        if health == 0:
            print('You have no more health a monster has got you... GAME OVER!')
            break
        else:
            print("You have" + str(health) + "lives left")
        

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
