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
def extract_data(room_num):
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

def show_data(room_num):
    print("\n" + room[room_num][0] + room[room_num][1])
    print("Enemy Details")
    print("Name:", enemy[room_num][0])
    print("Damage:", enemy[room_num][1])
    print("Health:", enemy[room_num][2])

# Reading Files and Extracting the Data
with open("Adventure_Game/Room1.txt", "r") as r1File:
    room["room1"] = r1File.readlines()
    extract_data("room1")
            
with open("Adventure_Game/Room2.txt", "r") as r2File:
    room["room2"] = r2File.readlines()
    extract_data("room2")

with open("Adventure_Game/Room3.txt", "r") as r3File:
    room["room3"] = r3File.readlines()
    extract_data("room3")

with open("Adventure_Game/Room4.txt", "r") as r4File:
    room["room4"] = r4File.readlines()
    extract_data("room4")

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

# Functions for displaying
def r1_show():
    show_data("room1")

def r2_show():
    show_data("room2")

def r3_show():
    show_data("room3")

def r4_show():
    show_data("room4")

def shop_show(balance):
    print("\nWelcome to the shop!", name)
    print("What do you want to buy? \n1. Weapons\n2. Key\n3.Healing Pad\n4. Armour")
    ans = input("Your answer (1,2,3,4): ")
    if ans =="1":
        print("Here are the weapons", name, "{Weapon description: [name, damage, price]}")
        print(shop_items["weapon"])
        weapon_num = input("Which weapon do you want to buy? Your answer (1/2/3/...): ")
        inventory["weapon"] = shop_items["weapon"]["weapon"+weapon_num]
        balance-=int(shop_items["weapon"]["weapon"+weapon_num][-1])
        playerBalance.configure(text= "string: "+ str(balance))
        
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
room1 = tkinter.Button(frame, text= "Room 1", command = r1_show, fg= "white", bg= "red", font = ('Calibri, 12'))
room1.grid(row = 0, column = 0, padx= 10)
room2 = tkinter.Button(frame, text= "Room 2", command = r2_show, fg= "white", bg= "green", font = ('Calibri, 12'))
room2.grid(row = 0, column = 1, padx= 10)
room3 = tkinter.Button(frame, text= "Room 3", command = r3_show, fg= "white", bg= "blue", font = ('Calibri, 12'))
room3.grid(row = 0, column = 2, padx= 10)
room4 = tkinter.Button(frame, text= "Room 4", command = r4_show, fg= "white", bg= "black", font = ('Calibri, 12'))
room4.grid(row = 0, column = 3, padx= 10)

frame2 = tkinter.Frame(window)
frame2.pack(anchor = "n", padx = 10, pady =15)
shop = tkinter.Button(frame2, text= "Shop", command =lambda:shop_show(balance), fg= "black", bg= "yellow",font= ('Calibri, 12'))
shop.grid(row = 0, column = 0, padx= 10)
myInventory = tkinter.Button(frame2, text= "My Inventory", command=inventory_show, fg= "black", bg= "yellow",font= ('Calibri, 12'))
myInventory.grid(row = 0, column = 1, padx= 10)

window.mainloop()