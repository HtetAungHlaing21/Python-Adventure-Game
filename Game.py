# Text-Based Adventure Game

# Libraries
import tkinter #For GUI
import random #For random money

# Variable Section Starts

# Balance, health and points of the player
balance = random.randint(200, 500)
health = 100
points = 0

# The empty datasets to store the data from rooms, shop, inventory and battle items
room = {"room1": [],"room2": [], "room3": [],"room4": []}
enemy = {"room1": [],"room2": [], "room3": [],"room4": []}
point = {"room1": [],"room2": [], "room3": [],"room4": []}
weapon = {"room1": [],"room2": [], "room3": [],"room4": []}
money = {"room1": [],"room2": [], "room3": [],"room4": []}
others = {"room1": {},"room2": {}, "room3": {},"room4": {}}
shop_items = {"weapon": {}, "key" : {}, "healing pad": [0, 0], "armour": {}}
inventory = {"weapon": {}, "key": {}, "healing pad": 0, "armour": {}, "treasure" : {}}
battle_items = {"weapon" : {}, "armour" : {}}
battle_items_name =[]

# Functions Start.

# Reading room files and Extracting the Data
def read_files(room_num):
    with open("" + room_num.capitalize() + ".txt", "r") as myFile:
        room[room_num] = myFile.readlines()
        for index, line in enumerate(room[room_num]):
            if "#" in line:
                temp = (room[room_num][index+1]).strip()
                if "Enemy" in line:
                    enemy[room_num] = temp.split(',')
                if "Point" in line:
                    point[room_num] = temp
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

# Reading shop files and Extracting the data
def read_shop():
    original_key=1
    with open("Shop.txt", "r") as my_shop:
        shop_wholetext = my_shop.readlines()
        for index, line in enumerate(shop_wholetext):
            temp = shop_wholetext[index].strip()
            if "weapon" in shop_wholetext[index]:
                temp = temp.split(':')
                shop_items["weapon"][temp[0]] = (temp[1]).split(',')
            if "key" in shop_wholetext[index]:
                temp = temp.split(':')
                temp2 = temp[1].split(',')
                shop_items["key"][temp[0]+str(original_key)] = temp2
            if "HealingPad" in line:
                heal = line.split(" ")
                shop_items["healing pad"][0] = shop_wholetext[index+1].strip()
                shop_items["healing pad"][1] = heal[-1].strip()
            if "armour" in shop_wholetext[index]:
                temp = temp.split(':')
                shop_items["armour"][temp[0]] = (temp[1]).split(',')

# Displaying the data of the room
def room_show(room_num):
    if int(enemy[room_num][2]) > 0 and points>=0 and points<10:
        room_GUI = tkinter.Tk() #A new room_GUI
        room_GUI.geometry("1000x700") #Setting the width and height
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
        fight = tkinter.Button(options, text="Fight!", command=lambda:fight_function(options,message, room_num, room_GUI), bg= "red", fg= "white", font = ('Calibri, 12') )
        fight.grid(row=0, column=0, padx= 10)
        run = tkinter.Button(options, text="Run Away!",command=lambda:runAway_function(room_GUI), bg= "green", fg= "white", font = ('Calibri, 12') )
        run.grid(row=0, column=1, padx= 10)
        message = tkinter.Label(room_GUI, text = "", font = ('Calibri, 12'), fg="red")
        message.pack(pady = 5)
    elif int(enemy[room_num][2]) <= 0:
        messagebox.config(text="You have won this battle. You cannot enter this city again!")
    elif points>=10 or points<0:
        messagebox.config(text="You cannot enter this city now!!!")

# Planning to enter the room and fight
def fight_function(options,message, room, room_GUI):
    weapon_choose = tkinter.Button(options, text="Choose Weapons",command=lambda:weapon_choose_function(options,message, room, room_GUI), bg= "white", fg= "red", font = ('Calibri, 12') )
    weapon_choose.grid(row=1, column=0, padx= 10, pady= 30)
    armour_choose = tkinter.Button(options, text="Choose Armours",command=lambda:armour_choose_function(options,message), bg= "white", fg= "red", font = ('Calibri, 12') )
    armour_choose.grid(row=1, column=1, padx= 10, pady= 30)

# Asking the player to choose the weapon
def weapon_choose_function(options, message, room, room_GUI):
    weapons = tkinter.Label(options, text= "Weapons - " + str(inventory["weapon"]), font = ('Calibri, 12') )
    weapons.grid(row=2, column=0, padx= 10)
    if len(inventory["weapon"]) >0:
        weapon_ques = tkinter.Label(options, text="Choose your weapon! Write weapon1/weapon2 ...", font = ('Calibri, 11'))
        weapon_ques.grid(row=3, column=0, pady=5)
        weapon_ans = tkinter.Entry(options)
        weapon_ans.grid(row=4, column=0, pady=5)
        weapon_ans.insert(0, "weapon")
        weapon_ans.icursor(tkinter.END)
        answer = tkinter.Button(options, text="Select", fg="red", bg="white", command=lambda:select_weapon(weapon_ans, message, options, room, room_GUI), font= ('Calibri, 12'))
        answer.grid(row=5, column=0, pady=5)
    else:
        message.config(text="You have no weapons. Buy more in the shop!")

# Asking the player to choose the armour
def armour_choose_function(options,message):
    armours = tkinter.Label(options, text= "Armours - " + str(inventory["armour"]), font = ('Calibri, 12'))
    armours.grid(row=2, column=1, padx=10)
    if len(inventory["armour"])>0:
        armour_ques = tkinter.Label(options, text="Choose your armour! Write armour1/armour2 ...", font = ('Calibri, 11'))
        armour_ques.grid(row=3, column=1, pady=5)
        armour_ans = tkinter.Entry(options)
        armour_ans.grid(row=4, column=1, pady=5)
        armour_ans.insert(0, "armour")
        armour_ans.icursor(tkinter.END)
        answer = tkinter.Button(options, text="Select", fg="red", bg="white", command=lambda:select_armour(armour_ans, message) , font= ('Calibri, 12'))
        answer.grid(row=5, column=1, pady=5)
    else:
        message.config(text="You have no armours. Buy more in the shop!")

# The player selecting the weapon
def select_weapon(item, message, options, room, room_GUI):
    global battle_items, battle_items_name
    name = item.get()
    battle_items_name.insert(0, name)
    item.delete(len(name)-1, tkinter.END)
    try:
        battle_items["weapon"] = inventory["weapon"][name]
        start = tkinter.Button(options, text="Start the FIGHT!", command=lambda: start_fight(room, message, room_GUI), bg="red", fg="white", font = ('Calibri, 11'))
        start.grid(row=6, column=0, pady=10)
        message.config(text="Selected! Start the fight now!")
    except:
        message.config(text="No valid weapon! Type again correctly.")

# The player selecting the armour
def select_armour(item, message):
    global battle_items, battle_items_name
    name = item.get()
    battle_items_name.insert(1, name)
    item.delete(len(name)-1, tkinter.END)
    try:
        battle_items["armour"]= inventory["armour"][name]
        message.config(text="Selected!")
    except:
        message.config(text="No valid armour! Type again correctly.")

# Starting the fight
def start_fight(room, message, room_GUI):
    global battle_items, health, enemy, points, money, point, balance, battle_items_name, key_num, weapon_num, treasure_num
    enemy_health_recovery = enemy[room][2]
    enemy_health = int(enemy[room][2])
    enemy_damage = int(enemy[room][1])
    try:
        enemy_damage/=int(battle_items["armour"][0])
    except:
        pass
    while True:
        enemy_health -= int(battle_items["weapon"][1])
        if enemy_health<=0:
            points+=int(point[room])
            inventory["weapon"]["weapon" + str(weapon_num)] = weapon[room]
            weapon_num +=1
            balance += int(money[room])
            try:
                inventory["treasure"]["treasure"+str(treasure_num)] = others[room]["treasure"]
                treasure_num+=1
                open_treasure.pack(pady= 5)
            except:
                pass
            try:
                inventory["healing pad"] += int(others[room]["healing pad"])
            except:
                pass
            try:
                inventory["key"]["key"+str(key_num)] = others[room]["key"]
                key_num +=1
            except:
                pass
            message.config(text="Congratulations! You Won the Battle!")
            enemy[room][2] = str(enemy_health)
            break
        health -= enemy_damage
        if health<=0:
            enemy[room][2] = enemy_health_recovery
            points -=2
            health = 0
            message.config(text="You Lost the Battle!")
            break
    inventory["weapon"].pop(battle_items_name[0])
    try:
        inventory["armour"].pop(battle_items_name[1])
    except:
        pass
    playerHealth.configure(text = 'Health: ' + str(round(health,2)), font = ('Calibri, 12'))
    playerBalance.configure(text = 'Balance: ' + str(balance), font = ('Calibri, 12'))
    playerPoints.configure(text = 'Points: ' + str(points), font = ('Calibri, 12'))
    weapons_details.configure(text= "Weapons - " + str(inventory["weapon"]), font = ('Calibri, 12'))
    key_details.configure(text="Keys - " +   str(inventory["key"]), font = ('Calibri, 12'))
    healing_details.configure(text= "No: of healing pads - " +  str(inventory["healing pad"]), font = ('Calibri, 12'))
    armour_details.configure(text="Armours - " + str(inventory["armour"]), font = ('Calibri, 12'))
    treasure_details.configure(text="Treasure - " + str(inventory["treasure"]), font = ('Calibri, 12'))
    leave = tkinter.Button(room_GUI, text="Leave the Room", command=lambda: runAway_function(room_GUI), bg= "red", fg= "white", font = ('Calibri, 12') )
    leave.pack(padx= 10)
    if points<0:
        winorlose.configure(text="Game Over! You have got below zero points.", font = ('Calibri, 12'))
    if points>=10:
        winorlose.configure(text="Congratulations! You have got 10 points and you won the game!!", font = ('Calibri, 12'))

# Running away from the city without fighting
def runAway_function(room_GUI):
    global battle_items, battle_items_name
    room_GUI.destroy()
    battle_items = {}
    battle_items_name = []

# Displaying the data of the shop
def shop_show():
    if points>=0 and points<10:
        shop_window = tkinter.Tk() 
        shop_window.geometry("1500x800")
        shop_window.title("Shop")
        greeting = tkinter.Label(shop_window, text = 'Welcome to the shop!', font = ('Calibri, 14'))
        greeting.pack(pady = 5)
        chooseAction = tkinter.Frame(shop_window)
        chooseAction.pack(anchor = "n", padx = 10, pady =5)
        buyAction = tkinter.Button(chooseAction, text= 'BUY', command=lambda: shop_buy_show(shop_window),  fg= "white", bg= "green", font=('Calibri, 14') )
        buyAction.grid(row=0, column=0, padx=10, pady=5)
        sellAction = tkinter.Button(chooseAction, text= 'SELL', command=lambda: shop_sell_show(chooseAction) ,  fg= "white", bg= "red", font=('Calibri, 14') )
        sellAction.grid(row=0, column=1, padx=10, pady=5)
    else:
        messagebox.config(text="You cannot enter the shop now!!!")

# Shop GUI
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

# Showing item list in the shop
def item_list(shop_items, item, frame):
    i = 1
    if item == "weapon":
        for weapon in shop_items["weapon"]:
            weapon_details = tkinter.Label(frame, text= "Weapon "+ str(i) + ": Name: " + shop_items["weapon"][weapon][0] + ": Damage: " + shop_items["weapon"][weapon][1]+ ": Price: " + shop_items["weapon"][weapon][2], font = ('Calibri, 12'))
            weapon_details.grid(row=i, column=0,padx=10, pady=10)
            i+=1
        ask_num(frame, "Type a weapon number to buy.\nEg: weapon1/weapon2/weapon3/...", 0, i, "weapon")

    if item == "key":
        for key in shop_items["key"]:
            key_details = tkinter.Label(frame, text= key + ": Price: " + shop_items["key"][key][1] , font = ('Calibri, 12'))
            key_details.grid(row=i, column=1, padx=10, pady=10)
            i+=1
        ask_num(frame, "Type a key number to buy.\nEg; key0/key1/ ...", 1, i, "key")

    if item == "heal":
        heal_details = tkinter.Label(frame, text= "Price: " + shop_items["healing pad"][1] + "    Left: " + str(shop_items["healing pad"][0]) , font = ('Calibri, 12'))
        heal_details.grid(row=i, column=2, padx=10, pady=10)
        ask_num(frame, "Do you want to buy healing pad? If yes, click 'Buy'.", 2, 1, "heal")

    if item == "armour":
        for armour in shop_items["armour"]:
            armour_details = tkinter.Label(frame, text= "Armour "+ str(i)+ ": Durability: " + shop_items["armour"][armour][0] + ": Price: " + shop_items["armour"][armour][1] , font = ('Calibri, 12'))
            armour_details.grid(row=i, column=3, padx=10, pady=10)
            i+=1
        ask_num(frame, "Type a armour number to buy\nEg: armour1/armour2/...", 3, i, "armour")
    
# Asking the items to buy
def ask_num(frame, text, column, i, prompt):
    buy_ques = tkinter.Label(frame, text= text , font = ('Calibri, 12'))
    buy_ques.grid(row=i+1, column=column, padx=10, pady=20)
    buy_ans = tkinter.Entry(frame)
    buy_ans.grid(row=i+2, column=column, padx=10, pady=5)
    buy_ans.insert(0, prompt)
    buy_ans.icursor(tkinter.END)
    send = tkinter.Button(frame, text = "Buy", command=lambda: buy(buy_ans, message), fg = "white", bg= "green", font = ('Calibri, 12'))
    send.grid(row =i+3, column= column, pady=5)
    message = tkinter.Label(frame, text = "", font = ('Calibri, 12'), fg='red')
    message.grid(row =i+4, column= column, pady=5)

# Buying items (weapons, keys and armours)
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

# Buying healing pad
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

# Actual buying process
def buy(buy_ans, message):
    global balance
    ans = buy_ans.get()
    if ans != 'heal':
        buy_ans.delete(len(ans)-1, tkinter.END)
    if ans not in inventory["armour"] and ans not in inventory["weapon"] and ans not in inventory["key"]:
        if "weapon" in ans or 'key' in ans or ans == 'heal' or "armour" in ans:
            if 'weapon' in ans:
                buy_items("weapon", ans, message)
            if 'key' in ans:
                buy_items("key", ans, message)
            if ans == 'heal':
                buy_heal(message)
            if 'armour' in ans:
                buy_items("armour", ans, message)
        else:
            message.config(text="Purchase Failed! Type again correctly.")
    else:
        message.config(text="Purchase Failed! It is already in your inventory.")

# Asking the player what he/she wants to sell
def shop_sell_show(place):
    question = tkinter.Label(place, text= "Type the item you want to sell.",font = ('Calibri, 12') )
    question.grid(row = 2, column=1, padx = 20, pady=20)
    example = tkinter.Label(place, text="Eg; weapon1, key0, heal, armour1, ....", font = ('Calibri, 12'))
    example.grid(row=3, column=1, padx=20, pady=10)
    text = tkinter.Entry(place)
    text.grid(row=4, column = 1, padx= 20, pady=10)
    sellbtn = tkinter.Button(place, text="Sell", command=lambda:sell_items(message, text) , fg= "white", bg= "green", font = ('Calibri, 12'))
    sellbtn.grid(row=5, column=1, padx=20, pady=10)
    message = tkinter.Label(place, text="", font = ('Calibri, 12'), fg="red")
    message.grid(row=6, column=1, padx=20, pady=10)

# Selling items
def sell_items(message, text):
    global inventory, balance, shop_items
    item = text.get()
    text.delete(0, tkinter.END)
    try:
        if item in inventory["weapon"] or item in inventory["armour"] or item in inventory["key"]:
            if "weapon" in item:
                balance += int(inventory["weapon"][item][-1])
                inventory['weapon'].pop(item)
                weapons_details.configure(text= "Weapons - " + str(inventory["weapon"]), font = ('Calibri, 12'))
            if "armour" in item:
                balance += int(inventory["armour"][item][-1])
                inventory['armour'].pop(item)
                armour_details.configure(text="Armours - " + str(inventory["armour"]), font = ('Calibri, 12'))
            if "key" in item:
                balance += int(inventory["key"][item][-1])
                inventory['key'].pop(item)
                key_details.configure(text="Keys - " + str(inventory["key"]), font = ('Calibri, 12'))             
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

# Using the healing pad
def use_heal():
    global health
    if inventory["healing pad"]>0:
        if health <= 50:
            health +=50
        else:
            health = 100
        inventory["healing pad"] -=1
        healing_details.configure(text= "No: of healing pads - " +  str(inventory["healing pad"]), font = ('Calibri, 12'))
        playerHealth.configure(text = 'Health: ' + str(round(health,2)), font = ('Calibri, 12'))
        messagebox.configure(text= "Successfully Healed!", font = ('Calibri, 12'))
    else:
        messagebox.configure(text="You have no healing pads.", font = ('Calibri, 12'))

# Starting the game
def start_game(name_entry):
    playerName.pack(pady = 5)
    userName = name_entry.get()
    name_entry.delete(0, tkinter.END)
    playerBalance.pack(pady = 5)
    playerHealth.pack(pady = 5)
    playerPoints.pack(pady = 5)
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
    treasure_details.pack(pady = 5)
    messagebox.pack(pady=5)
    winorlose.pack(pady=5)
    quitGame = tkinter.Button(window, text="Quit Game", command=quit_game, fg="white", bg="red", font=('Calibri, 12'))
    quitGame.pack(pady=5)
    resetGame = tkinter.Button(window, text="Reset Game", command=reset_game, fg="white", bg="green", font=('Calibri, 12'))
    resetGame.pack(pady=5)

# Quitting the game
def quit_game():
    window.destroy();
    print("\nThanks for playing adventure game! See you again!\n")

# Resetting the game
def reset_game():
    global balance, health, points, inventory, key_num, weapon_num, treasure_num
    balance = random.randint(200, 500)
    health = 100
    points = 0
    inventory = {"weapon": {}, "key": {}, "healing pad": 0, "armour": {}, "treasure" : {}}
    playerBalance.config(text = 'Balance: ' + str(balance), font =  ('Calibri, 12'))
    playerHealth.config(text = 'Health: ' + str(round(health,2)), font = ('Calibri, 12') )
    playerPoints.config(text = 'Points: ' + str(points), font = ('Calibri, 12') )
    read_files("room1")
    read_files("room2")
    read_files("room3")
    read_files("room4")
    read_shop()
    key_num =  len(shop_items["key"]) + 1;
    weapon_num = len(shop_items["weapon"]) + 1;
    treasure_num = 1
    weapons_details.configure(text= "Weapons - " + str(inventory["weapon"]), font = ('Calibri, 12'))
    key_details.configure(text="Keys - " +   str(inventory["key"]), font = ('Calibri, 12'))
    healing_details.configure(text= "No: of healing pads - " +  str(inventory["healing pad"]), font = ('Calibri, 12'))
    armour_details.configure(text="Armours - " + str(inventory["armour"]), font = ('Calibri, 12'))
    treasure_details.configure(text= "", font = ('Calibri, 12'))
    messagebox.configure(text="Game Resetted!" , font = ('Calibri, 12'))
    winorlose.configure(text="")

# Opening treasure box
def open_treasure_box():
    global inventory, points
    if len(inventory["key"]) == 0:
        messagebox.config(text="No keys to collect treasure box!")
    for item in inventory["treasure"]:
        for key in inventory["key"]:
            if inventory["treasure"][item][0] == inventory["key"][key][0]:
                points += int(inventory["treasure"][item][1])
                inventory["treasure"].pop(item)
                inventory["key"].pop(key)
                messagebox.config(text="Points collected! Click again if you have more treasure boxes.")
                break
            else:
                messagebox.config(text="The keys do not match the treasure box!")                
        break
    playerPoints.config(text="Points: " + str(points), font = ('Calibri, 12'))
    treasure_details.configure(text="Treasure - " + str(inventory["treasure"]), font = ('Calibri, 12'))
    key_details.configure(text="Keys - " + str(inventory["key"]), font = ('Calibri, 12'))
    if points<0:
        winorlose.configure(text="Game Over! You have got below zero points.", font = ('Calibri, 12'))
    if points>=10:
        winorlose.configure(text="Congratulations! You have got 10 points and you won the game!!", font = ('Calibri, 12'))
# Functions end.

# The program starts from here.
# GUI
window = tkinter.Tk() #A new window
window.geometry("1000x800") #Setting the width and height
window.title("Adventure Game") #Title

# Welcome message
greeting = tkinter.Label(window, text = 'Welcome to Adventure World!', font = ('Calibri, 14'))
greeting.pack(pady = 5)

# A new frame to store the player's data
data = tkinter.Frame(window)
data.pack(anchor = "n", padx = 10, pady =15)

# Asking player's name
name = tkinter.Label(data, text="Enter your name", font = ('Calibri, 12'))
name.grid(row=0, column=0, pady = 5)
name_entry = tkinter.Entry(data)
name_entry.grid (row=0, column=1, pady=5)

# Start button
start = tkinter.Button(data, text= "Start", command = lambda:start_game(name_entry), fg= "black", bg= "yellow",font= ('Calibri, 12'))
start.grid(row = 0, column = 2, padx= 10)

# Player's Datas on GUI
playerName = tkinter.Label(window, font = ('Calibri, 12') )
playerBalance = tkinter.Label(window, text = 'Balance: ' + str(balance), font =  ('Calibri, 12'))
playerHealth = tkinter.Label(window, text = 'Health: ' + str(round(health,2)), font = ('Calibri, 12') )
playerPoints = tkinter.Label(window, text = 'Points: ' + str(points), font = ('Calibri, 12') )

# Inventory Data on GUI
intro = tkinter.Label(window, text= "Here is your inventory list! Visit the shop to buy more!", font = ('Calibri, 14'))
weapons_details = tkinter.Label(window, text= "", font = ('Calibri, 12'))
key_details = tkinter.Label(window, text= "", font = ('Calibri, 12'))
healing_details = tkinter.Label(window, text= "", font = ('Calibri, 12'))
armour_details = tkinter.Label(window, text= "", font = ('Calibri, 12'))
treasure_details = tkinter.Label(window, text= "", font = ('Calibri, 12'))
messagebox = tkinter.Label(window, text= "", fg="red", font = ('Calibri, 12'))
winorlose = tkinter.Label(window, text= "", fg="red", font = ('Calibri, 14'))
open_treasure = tkinter.Button(window, text="Open Treasure Box", command=open_treasure_box, fg="black", bg="yellow", font=('Calibri, 12'))

# Read 4 room files and shop
read_files("room1")
read_files("room2")
read_files("room3")
read_files("room4")
read_shop()

# Variables to track the keys, weapons and treasures in the room.
key_num = len(shop_items["key"]) + 1
weapon_num = len(shop_items["weapon"]) + 1
treasure_num = 1

# Showing GUI to the user
window.mainloop()