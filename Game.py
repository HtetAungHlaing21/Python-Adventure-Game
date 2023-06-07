# Text-Based Adventure Game

# Libraries
import tkinter #For GUI
import random #For random money

# Initializing variables
room = {"room1": [],"room2": [], "room3": [],"room4": []}
enemy = {"room1": [],"room2": [], "room3": [],"room4": []}
point = {"room1": [],"room2": [], "room3": [],"room4": []}
weapon = {"room1": [],"room2": [], "room3": [],"room4": []}
money = {"room1": [],"room2": [], "room3": [],"room4": []}
others = {"room1": {},"room2": {}, "room3": {},"room4": {}}
shop_items = {"weapon": {}, "key" : {}, "healing pad": [], "armour": {}}
inventory = {"weapon": {}, "key": {}, "armour": {}}

# Functions

# Reading Files and Extracting the Data
def read_files(room_num):
    with open("Adventure_Game/" + room_num.capitalize() + ".txt", "r") as myFile:
        room[room_num] = myFile.readlines()
        for index, line in enumerate(room[room_num]):
            if "#" in line:
                temp = (room[room_num][index+1]).strip()
                if "Enemy" in line:
                    enemy[room_num] = temp.split(',')
                if "Point" in line:
                    point[room_num] = temp.split(',')
                if "Weapon" in line:
                    weapon[room_num] = temp.split(',')
                if "Money" in line:
                    money[room_num] = temp
                if "Treasure" in line:
                    others[room_num]["treasure"] = temp.split(',')
                if "HealingPad" in line:
                    others[room_num]["healing pad"] = temp
                if "Key" in line:
                    others[room_num]["key"] = temp.split(',')

# Reading and Extracting the shop
def read_shop():
    with open("Adventure_Game/Shop.txt", "r") as my_shop:
        shop_wholetext = my_shop.readlines()
        for index, line in enumerate(shop_wholetext):
            temp = shop_wholetext[index].strip()
            if "weapon" in shop_wholetext[index]:
                temp = temp.split(':')
                shop_items["weapon"][temp[0]] = (temp[1]).split(',')
            if "key" in shop_wholetext[index]:
                temp = temp.split(':')
                shop_items["key"][temp[0]] = (temp[1]).split(',')
            if "HealingPad" in line:
                heal = line.split(" ")
                shop_items["healing pad"].append(heal[-1].strip())
                shop_items["healing pad"].append(shop_wholetext[index+1].strip())
            if "armour" in shop_wholetext[index]:
                temp = temp.split(':')
                shop_items["armour"][temp[0]] = (temp[1]).split(',')

# Displaying the data of the room
def room_show(room_num):
    read_files(room_num)
    print("\n" + room[room_num][0] + room[room_num][1])
    print("Enemy Details")
    print("Name:", enemy[room_num][0])
    print("Damage:", enemy[room_num][1])
    print("Health:", enemy[room_num][2])

# Displaying the data of the shop
def shop_show():
    read_shop()
    window = tkinter.Tk() #A new window
    window.geometry("1200x400") #Setting the width and height
    window.title("Shop") #Title
    greeting = tkinter.Label(window, text = 'Welcome to the shop!', font = ('Calibri, 14'))
    greeting.pack(pady = 5)
    question = tkinter.Label(window, text ="What do you want to buy?", font = ('Calibri, 14'))
    question.pack(pady= 5)
    playerBalance = tkinter.Label(window, text = 'Your Balance: ' + str(balance), font = ('Calibri, 12') )
    playerBalance.pack(pady = 5)
    frame = tkinter.Frame(window)
    frame.pack(anchor = "n", padx = 10, pady =5)
    weapon = tkinter.Button(frame, text= "Weapons", command=lambda: item_list(shop_items, "weapon", frame), fg= "white", bg= "blue", font = ('Calibri, 12'))
    weapon.grid(row = 0, column = 0, padx= 10)
    key = tkinter.Button(frame, text= "Key", fg= "white",command=lambda: item_list(shop_items, "key", frame), bg= "red", font = ('Calibri, 12'))
    key.grid(row = 0, column = 1, padx= 10)
    healingPad = tkinter.Button(frame, text= "Healing Pad", command=lambda: item_list(shop_items, "heal", frame), fg= "white", bg= "green", font = ('Calibri, 12'))
    healingPad.grid(row = 0, column = 2, padx= 10)
    armour = tkinter.Button(frame, text= "Armours", command=lambda: item_list(shop_items, "armour", frame), fg= "black", bg= "pink", font = ('Calibri, 12'))
    armour.grid(row = 0, column = 3, padx= 10)
    
    #     print("Here are the weapons", name, "{Weapon description: [name, damage, price]}")
    #     print(shop_items["weapon"])
    #     weapon_num = input("Which weapon do you want to buy? Your answer (1/2/3/...): ")
    #     inventory["weapon"] = shop_items["weapon"]["weapon"+weapon_num]
    #     balance-=int(shop_items["weapon"]["weapon"+weapon_num][-1])
    #     playerBalance.configure(text= "string: "+ str(balance))

# Show item list in the shop
def item_list(shop_items, item, frame):
    i = 1
    if item == "weapon":
        for weapon in shop_items["weapon"]:
            weapon_details = tkinter.Label(frame, text= "Weapon "+ str(i) + ": Name: " + shop_items["weapon"][weapon][0] + ": Damage: " + shop_items["weapon"][weapon][1]+ ": Price: " + shop_items["weapon"][weapon][2], font = ('Calibri, 12'))
            weapon_details.grid(row=i, column=0,padx=10, pady=10)
            i+=1
    if item == "key":
        for key in shop_items["key"]:
            key_details = tkinter.Label(frame, text= "Key "+ str(i) + ": Price: " + shop_items["key"][key][1] , font = ('Calibri, 12'))
            key_details.grid(row=i, column=1, padx=10, pady=10)
            i+=1
    if item == "heal":
        heal_details = tkinter.Label(frame, text= "Price: " + shop_items["healing pad"][0] + "    Left: " + shop_items["healing pad"][1] , font = ('Calibri, 12'))
        heal_details.grid(row=i, column=2, padx=10, pady=10)
    if item == "armour":
        for armour in shop_items["armour"]:
            armour_details = tkinter.Label(frame, text= "Armour "+ str(i)+ ": Durability: " + shop_items["armour"][armour][0] + ": Price: " + shop_items["armour"][armour][1] , font = ('Calibri, 12'))
            armour_details.grid(row=i, column=3, padx=10, pady=10)
            i+=1

# Displaying the player's inventory
def inventory_show():
    print("\nHere is your inventory list! Visit the shop to buy more!")
    print(inventory)


# Asking the player's name and setting the default values
name = input("Enter your name: ")
balance = random.randint(50, 310)
health = 100
points = 0


# GUI
window = tkinter.Tk() #A new window
window.geometry("400x400") #Setting the width and height
window.title("Adventure Game") #Title

# Welcome message & Initial Data
greeting = tkinter.Label(window, text = 'Welcome to Adventure World!', font = ('Calibri, 14'))
greeting.pack(pady = 5)

playerName = tkinter.Label(window, text = 'Name: ' + name, font = ('Calibri, 12') )
playerName.pack(pady = 5)

playerBalance = tkinter.Label(window, text = 'Balance: ' + str(balance), font = ('Calibri, 12') )
playerBalance.pack(pady = 5)

playerHealth = tkinter.Label(window, text = 'Health: ' + str(health), font = ('Calibri, 12') )
playerHealth.pack(pady = 5)

playerPoints = tkinter.Label(window, text = 'Points: ' + str(points), font = ('Calibri, 12') )
playerPoints.pack(pady = 5)

# Buttons
frame = tkinter.Frame(window)
frame.pack(anchor = "n", padx = 10, pady =15)
room1 = tkinter.Button(frame, text= "Room 1", command = lambda: room_show("room1"), fg= "white", bg= "red", font = ('Calibri, 12'))
room1.grid(row = 0, column = 0, padx= 10)
room2 = tkinter.Button(frame, text= "Room 2", command = lambda: room_show("room2"), fg= "white", bg= "green", font = ('Calibri, 12'))
room2.grid(row = 0, column = 1, padx= 10)
room3 = tkinter.Button(frame, text= "Room 3", command = lambda: room_show("room3"), fg= "white", bg= "blue", font = ('Calibri, 12'))
room3.grid(row = 0, column = 2, padx= 10)
room4 = tkinter.Button(frame, text= "Room 4", command = lambda: room_show("room4"), fg= "white", bg= "black", font = ('Calibri, 12'))
room4.grid(row = 0, column = 3, padx= 10)

frame2 = tkinter.Frame(window)
frame2.pack(anchor = "n", padx = 10, pady =15)
shop = tkinter.Button(frame2, text= "Shop", command = shop_show, fg= "black", bg= "yellow",font= ('Calibri, 12'))
shop.grid(row = 0, column = 0, padx= 10)
myInventory = tkinter.Button(frame2, text= "My Inventory", command=inventory_show, fg= "black", bg= "yellow",font= ('Calibri, 12'))
myInventory.grid(row = 0, column = 1, padx= 10)

window.mainloop()