# Text-Based Adventure Game

# Libraries
import tkinter #For GUI
import random #For random money

# GUI
window = tkinter.Tk() #A new window
window.geometry("700x700") #Setting the width and height
window.title("Adventure Game") #Title

# Asking the player's name and setting the default values
# balance = random.randint(50, 310)
balance = 300
health = 100
points = 0

# Initializing variables
room = {"room1": [],"room2": [], "room3": [],"room4": []}
enemy = {"room1": [],"room2": [], "room3": [],"room4": []}
point = {"room1": [],"room2": [], "room3": [],"room4": []}
weapon = {"room1": [],"room2": [], "room3": [],"room4": []}
money = {"room1": [],"room2": [], "room3": [],"room4": []}
others = {"room1": {},"room2": {}, "room3": {},"room4": {}}
shop_items = {"weapon": {}, "key" : {}, "healing pad": [], "armour": {}}
inventory = {"weapon": {}, "key": {}, "healing pad": 0, "armour": {}}
battle_items = {}

# Datas on GUI
playerName = tkinter.Label(window, font = ('Calibri, 12') )
playerBalance = tkinter.Label(window, text = 'Balance: ' + str(balance), font = ('Calibri, 12') )
playerHealth = tkinter.Label(window, text = 'Health: ' + str(health), font = ('Calibri, 12') )
playerPoints = tkinter.Label(window, text = 'Points: ' + str(points), font = ('Calibri, 12') )

# Inventory Data on GUI
intro = tkinter.Label(window, text= "Here is your inventory list! Visit the shop to buy more!", font = ('Calibri, 14'))
weapons_details = tkinter.Label(window, text= "", font = ('Calibri, 12'))
key_details = tkinter.Label(window, text= "", font = ('Calibri, 12'))
healing_details = tkinter.Label(window, text= "", font = ('Calibri, 12'))
armour_details = tkinter.Label(window, text= "", font = ('Calibri, 12'))
messagebox = tkinter.Label(window, text= "", fg="red", font = ('Calibri, 12'))

# Functions
# Reading Files and Extracting the Data
def read_files(room_num):
    with open("" + room_num.capitalize() + ".txt", "r") as myFile:
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
    with open("Shop.txt", "r") as my_shop:
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
                shop_items["healing pad"].append(shop_wholetext[index+1].strip())
                shop_items["healing pad"].append(heal[-1].strip())
            if "armour" in shop_wholetext[index]:
                temp = temp.split(':')
                shop_items["armour"][temp[0]] = (temp[1]).split(',')

# Displaying the data of the room
def room_show(room_num):
    read_files(room_num)
    room_GUI = tkinter.Tk() #A new room_GUI
    room_GUI.geometry("700x700") #Setting the width and height
    room_GUI.title(room_num.capitalize()) #Title
    greeting = tkinter.Label(room_GUI, text = room[room_num][0] + room[room_num][1], font = ('Calibri, 14'))
    greeting.pack(pady = 5)
    enemy_title = tkinter.Label(room_GUI, text = "Enemy Details", font = ('Calibri, 14'))
    enemy_title.pack(pady = 5)
    enemy_name = tkinter.Label(room_GUI, text = "Name:" + enemy[room_num][0], font = ('Calibri, 12'))
    enemy_name.pack(pady = 5)
    enemy_damage = tkinter.Label(room_GUI, text = "Damage:"+ enemy[room_num][1], font = ('Calibri, 12'))
    enemy_damage.pack(pady = 5)
    enemy_health = tkinter.Label(room_GUI, text = "Health:"+ enemy[room_num][2], font = ('Calibri, 12'))
    enemy_health.pack(pady = 5)
    options = tkinter.Frame(room_GUI)
    options.pack(pady= 10)
    fight = tkinter.Button(options, text="Fight!", command=lambda:fight_function(options,message), bg= "red", fg= "white", font = ('Calibri, 12') )
    fight.grid(row=0, column=0, padx= 10)
    run = tkinter.Button(options, text="Run Away!",command=lambda:runAway_function(room_GUI), bg= "green", fg= "white", font = ('Calibri, 12') )
    run.grid(row=0, column=1, padx= 10)
    message = tkinter.Label(room_GUI, text = "", font = ('Calibri, 12'), fg="red")
    message.pack(pady = 5)

def fight_function(options,message):
    weapon_choose = tkinter.Button(options, text="Choose Weapons",command=lambda:weapon_choose_function(options,message), bg= "white", fg= "red", font = ('Calibri, 12') )
    weapon_choose.grid(row=1, column=0, padx= 10, pady= 30)
    armour_choose = tkinter.Button(options, text="Choose Armours",command=lambda:armour_choose_function(options,message), bg= "white", fg= "red", font = ('Calibri, 12') )
    armour_choose.grid(row=1, column=1, padx= 10, pady= 30)

def weapon_choose_function(options, message):
    weapons = tkinter.Label(options, text= "Weapons - " + str(inventory["weapon"]), font = ('Calibri, 12') )
    weapons.grid(row=2, column=0, padx= 10)
    if len(inventory["weapon"]) >0:
        weapon_ques = tkinter.Label(options, text="Choose your weapon! Write weapon1/weapon2 ...", font = ('Calibri, 11'))
        weapon_ques.grid(row=3, column=0, pady=5)
        weapon_ans = tkinter.Entry(options)
        weapon_ans.grid(row=4, column=0, pady=5)
        answer = tkinter.Button(options, text="Select", fg="red", bg="white", command=lambda:select_items("weapon", weapon_ans, message, options), font= ('Calibri, 12'))
        answer.grid(row=5, column=0, pady=5)
    else:
        message.config(text="You have no weapons. Buy more in the shop!")

def armour_choose_function(options,message):
    armours = tkinter.Label(options, text= "Armours - " + str(inventory["armour"]), font = ('Calibri, 12'))
    armours.grid(row=2, column=1, padx=10)
    if len(inventory["armour"])>0:
        armour_ques = tkinter.Label(options, text="Choose your armour! Write armour1/armour2 ...", font = ('Calibri, 11'))
        armour_ques.grid(row=3, column=1, pady=5)
        armour_ans = tkinter.Entry(options)
        armour_ans.grid(row=4, column=1, pady=5)
        answer = tkinter.Button(options, text="Select", fg="red", bg="white", command=lambda:select_items("armour", armour_ans, message, options) , font= ('Calibri, 12'))
        answer.grid(row=5, column=1, pady=5)
    else:
        message.config(text="You have no armours. Buy more in the shop!")

def select_items(item_name, item, message, options):
    global battle_items
    name = item.get()
    item.delete(0, tkinter.END)
    if item_name == "weapon":
        try:
            battle_items[name] = inventory["weapon"][name]
            start = tkinter.Button(options, text="Start the FIGHT!", command=start_fight, bg="red", fg="white", font = ('Calibri, 11'))
            start.grid(row=6, column=0, pady=10)
            message.config(text="Selected! Start the fight now!")
        except:
            message.config(text="No valid weapon! Type again correctly.")
    elif item_name == "armour":
        try:
            battle_items[name] = inventory["armour"][name]
            message.config(text="Selected!")
        except:
            message.config(text="No valid armour! Type again correctly.")

def start_fight():
    global battle_items
    print(battle_items)

def runAway_function(room_GUI):
    global battle_items
    room_GUI.destroy()
    battle_items = {}

# Displaying the data of the shop
def shop_show():
    read_shop()
    shop_window = tkinter.Tk() #A new shop_window
    shop_window.geometry("1500x800") #Setting the width and height
    shop_window.title("Shop") #Title
    greeting = tkinter.Label(shop_window, text = 'Welcome to the shop!', font = ('Calibri, 14'))
    greeting.pack(pady = 5)
    chooseAction = tkinter.Frame(shop_window)
    chooseAction.pack(anchor = "n", padx = 10, pady =5)
    buyAction = tkinter.Button(chooseAction, text= 'BUY', command=lambda: shop_buy_show(shop_window),  fg= "white", bg= "green", font=('Calibri, 14') )
    buyAction.grid(row=0, column=0, padx=10, pady=5)
    sellAction = tkinter.Button(chooseAction, text= 'SELL', command=lambda: shop_sell_show(chooseAction) ,  fg= "white", bg= "red", font=('Calibri, 14') )
    sellAction.grid(row=0, column=1, padx=10, pady=5)


def shop_buy_show(shop_window):
    question = tkinter.Label(shop_window, text ="What do you want to buy?", font = ('Calibri, 14'))
    question.pack(pady= 5)
    frame = tkinter.Frame(shop_window)
    frame.pack(anchor = "n", padx = 10, pady =5)
    weapon = tkinter.Button(frame, text= "Weapons", command=lambda: item_list(shop_items, "weapon", frame), fg= "white", bg= "blue", font = ('Calibri, 12'))
    weapon.grid(row = 0, column = 0, padx= 10)
    key = tkinter.Button(frame, text= "Key", fg= "white",command=lambda: item_list(shop_items, "key", frame), bg= "red", font = ('Calibri, 12'))
    key.grid(row = 0, column = 1, padx= 10)
    healingPad = tkinter.Button(frame, text= "Healing Pad", command=lambda: item_list(shop_items, "heal", frame), fg= "white", bg= "green", font = ('Calibri, 12'))
    healingPad.grid(row = 0, column = 2, padx= 10)
    armour = tkinter.Button(frame, text= "Armours", command=lambda: item_list(shop_items, "armour", frame), fg= "black", bg= "pink", font = ('Calibri, 12'))
    armour.grid(row = 0, column = 3, padx= 10)
    
def shop_sell_show(place):
    question = tkinter.Label(place, text= "Type the item you want to sell.",font = ('Calibri, 12') )
    question.grid(row = 2, column=1, padx = 20, pady=20)
    example = tkinter.Label(place, text="Eg; weapon1, heal, armour1, .... ( Note: Keys cannot be sold! )", font = ('Calibri, 12'))
    example.grid(row=3, column=1, padx=20)
    text = tkinter.Entry(place)
    text.grid(row=4, column = 1, padx= 20)
    sellbtn = tkinter.Button(place, text="Sell", command=lambda:sell_items(message, text) , fg= "white", bg= "green", font = ('Calibri, 12'))
    sellbtn.grid(row=5, column=1, padx=20)
    message = tkinter.Label(place, text="", font = ('Calibri, 12'))
    message.grid (row=6, column=1, padx=20, pady=10)
    
def sell_items(message, text):
    global inventory, balance, shop_items
    item = text.get()
    text.delete(0, tkinter.END)
    try:
        if item in inventory["weapon"] or item in inventory["armour"]:
            if "weapon" in item:
                inventory['weapon'].pop(item)
                balance += int(shop_items["weapon"][item][-1])
                weapons_details.configure(text= "Weapons - " + str(inventory["weapon"]), font = ('Calibri, 12'))
            if "armour" in item:
                inventory['armour'].pop(item)
                balance += int(shop_items["armour"][item][-1])
                armour_details.configure(text="Armours - " + str(inventory["armour"]), font = ('Calibri, 12'))                
            playerBalance.config(text= 'Balance: ' + str(balance))
            message.configure(text="Successfully Sold!")
        elif "heal" in item and inventory['healing pad']>0:
            inventory["healing pad"]-=1
            shop_items["healing pad"][0] = int(shop_items["healing pad"][0]) + 1
            balance+=int(shop_items["healing pad"][-1])
            healing_details.configure(text= "No: of healing pads - " +  str(inventory["healing pad"]), font = ('Calibri, 12'))
            playerBalance.config(text= 'Balance: ' + str(balance))
            message.configure(text="Successfully Sold!")
        else:
            message.configure(text="No such item in your inventory!")
    except:
        message.configure(text="No such item in your inventory!")

# Show item list in the shop
def item_list(shop_items, item, frame):
    i = 1
    if item == "weapon":
        for weapon in shop_items["weapon"]:
            weapon_details = tkinter.Label(frame, text= "Weapon "+ str(i) + ": Name: " + shop_items["weapon"][weapon][0] + ": Damage: " + shop_items["weapon"][weapon][1]+ ": Price: " + shop_items["weapon"][weapon][2], font = ('Calibri, 12'))
            weapon_details.grid(row=i, column=0,padx=10, pady=10)
            i+=1
        ask_num(frame, "Type a weapon number to buy.\nEg: weapon1/weapon2/weapon3/...", 0, i)

    if item == "key":
        for key in shop_items["key"]:
            key_details = tkinter.Label(frame, text= "Key "+ str(i) + ": Price: " + shop_items["key"][key][1] , font = ('Calibri, 12'))
            key_details.grid(row=i, column=1, padx=10, pady=10)
            i+=1
        ask_num(frame, "Do you want to buy a key? If yes, type 'key'. ", 1, i)

    if item == "heal":
        heal_details = tkinter.Label(frame, text= "Price: " + shop_items["healing pad"][1] + "    Left: " + str(shop_items["healing pad"][0]) , font = ('Calibri, 12'))
        heal_details.grid(row=i, column=2, padx=10, pady=10)
        ask_num(frame, "Do you want to buy healing pad? If yes, type 'heal'.", 2, 1)

    if item == "armour":
        for armour in shop_items["armour"]:
            armour_details = tkinter.Label(frame, text= "Armour "+ str(i)+ ": Durability: " + shop_items["armour"][armour][0] + ": Price: " + shop_items["armour"][armour][1] , font = ('Calibri, 12'))
            armour_details.grid(row=i, column=3, padx=10, pady=10)
            i+=1
        ask_num(frame, "Type a armour number to buy\nEg: armour1/armour2/...", 3, i)
    
# Asking the items to buy and buying process
def ask_num(frame, text, column, i):
    buy_ques = tkinter.Label(frame, text= text , font = ('Calibri, 12'))
    buy_ques.grid(row=i+1, column=column, padx=10, pady=20)
    buy_ans = tkinter.Entry(frame)
    buy_ans.grid(row=i+2, column=column, padx=10, pady=5)
    send = tkinter.Button(frame, text = "Buy", command=lambda: buy(buy_ans, message), fg = "white", bg= "green")
    send.grid(row =i+3, column= column)
    message = tkinter.Label(frame, text = "", font = ('Calibri, 12'))
    message.grid(row =i+4, column= column)

def buy_items(item_type, ans, message):
    global balance
    try:
        item = shop_items[item_type][ans]
        if balance - int(item[-1])>=0:
            inventory[item_type][ans] = item
            balance = balance - int(item[-1])
            playerBalance.config(text= 'Balance: ' + str(balance))
            if item_type == "weapon":
                weapons_details.configure(text= "Weapons - " + str(inventory["weapon"]), font = ('Calibri, 12'))
            if item_type == "key":
                key_details.configure(text="Keys - " +   str(inventory["key"]), font = ('Calibri, 12'))
            if item_type == "armour":
                armour_details.configure(text="Armours - " + str(inventory["armour"]), font = ('Calibri, 12'))
            message.config(text="Successfully Purchased! Check your inventory!!")
        else:
            message.config(text="Purchase Failed! Not enough money")
    except:
        message.config(text="Purchase Failed! Type again correctly.")

def buy_heal(message):
    global balance
    global shop_items
    item = shop_items["healing pad"]
    if balance-int(item[-1])>=0:
        inventory["healing pad"] += 1
        balance = balance - int(item[-1])
        playerBalance.config(text= 'Balance: ' + str(balance))
        message.config(text="Successfully Purchased! Check your inventory!!")
        healing_details.configure(text= "No: of healing pads - " +  str(inventory["healing pad"]), font = ('Calibri, 12'))
        shop_items["healing pad"][0] = int(shop_items["healing pad"][0])-1
    else:
        message.config(text="Purchase Failed! Not enough money")

def buy(buy_ans, message):
    global balance
    ans = buy_ans.get().lower()
    buy_ans.delete(0, tkinter.END)
    if "weapon" in ans or ans == 'key' or ans == 'heal' or "armour" in ans:
        if 'weapon' in ans:
            buy_items("weapon", ans, message)
        if ans == 'key':
            buy_items("key", ans, message)
        if ans == 'heal':
            buy_heal(message)
        if 'armour' in ans:
            buy_items("armour", ans, message)
    else:
        message.config(text="Purchase Failed! Type again correctly.")

def use_heal():
    global health
    if inventory["healing pad"]>0:
        if health <= 50:
            health +=50
        else:
            health = 100
        inventory["healing pad"] -=1
        healing_details.configure(text= "No: of healing pads - " +  str(inventory["healing pad"]), font = ('Calibri, 12'))
        playerHealth.configure(text = 'Health: ' + str(health), font = ('Calibri, 12'))
        messagebox.configure(text= "Successfully Healed!", font = ('Calibri, 12'))
    else:
        messagebox.configure(text="You have no healing pads.", font = ('Calibri, 12'))

# GUI
# Welcome message & Initial Data
greeting = tkinter.Label(window, text = 'Welcome to Adventure World!', font = ('Calibri, 14'))
greeting.pack(pady = 5)

data = tkinter.Frame(window)
data.pack(anchor = "n", padx = 10, pady =15)

name = tkinter.Label(data, text="Enter your name", font = ('Calibri, 12'))
name.grid(row=0, column=0, pady = 5)

name_entry = tkinter.Entry(data)
name_entry.grid (row=0, column=1, pady=5)

start = tkinter.Button(data, text= "Start", command = lambda:start_game(name_entry), fg= "black", bg= "yellow",font= ('Calibri, 12'))
start.grid(row = 0, column = 2, padx= 10)

def start_game(name_entry):
    playerName.pack(pady = 5)
    playerBalance.pack(pady = 5)
    playerHealth.pack(pady = 5)
    playerPoints.pack(pady = 5)
    userName = name_entry.get()
    name_entry.delete(0, tkinter.END)
    playerName.configure(text="Name: " + userName)
    # Delete the name section
    name.destroy()
    name_entry.destroy()
    start.destroy()
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
    shop = tkinter.Button(frame2, text= "Shop", command = lambda:shop_show(), fg= "black", bg= "yellow",font= ('Calibri, 12'))
    shop.grid(row = 0, column = 0, padx= 10)

    # Use the healing pad
    use_heal_btn = tkinter.Button(frame2, text="Use Healing Pad", command=use_heal, fg="white", bg="green" ,font = ('Calibri, 12'))
    use_heal_btn.grid(row=0, column=1, pady= 5)

    # My Inventory
    intro.pack(pady = 10)
    weapons_details.configure(text= "Weapons - " + str(inventory["weapon"]), font = ('Calibri, 12'))
    weapons_details.pack(pady = 5)
    key_details.configure(text="Keys - " +   str(inventory["key"]), font = ('Calibri, 12'))
    key_details.pack(pady = 5)
    healing_details.configure(text= "No: of healing pads - " +  str(inventory["healing pad"]), font = ('Calibri, 12'))
    healing_details.pack(pady = 5)
    armour_details.configure(text="Armours - " + str(inventory["armour"]), font = ('Calibri, 12'))
    armour_details.pack(pady = 5)
    messagebox.pack(pady=5)

window.mainloop()