################# Chapter 5 Dictionaries and Structuring Data

# myCat = {"size": "fat", "color": "gray", "disposition": "loud"}

# print(myCat["size"])
# birthday ={"Aigars": "2nd June", "Janis": "8th August"}

# while True:
#     print("Enter the name to get birthday, blank to quit: ")
#     name = input()
#     if name == "":
#         break
#     if name in birthday:
#         print("{0} is the birthday of {0}".format(birthday[name]), name)
#     else:
#         print("I dont have this information, please enter the date: ")
#         bday = input()
#         birthday[name] = bday
#         print("db updated")

# spam = {"name": "Pooka", "age": 5}
# if "color" not in spam:
#     spam["color"] = "black"
# print(spam)
# spam.setdefault("weight", 40)
# print(spam)


# import pprint

# message = "It was a bright cold day in April, and the clocks were triking thirteen."
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1

# pprint.pprint(count)
# print(pprint.pformat(count))

# theBoard = {"tL": " ", "tM": " ", "tR": " ",
#             "mL": " ", "mM": " ", "mR": " ",
#             "lL": " ", "lM": " ", "lR": " "}

# def printBoard(board):
#     print(board["tL"] + "|" + board["tM"] + "|" + board["tR"])
#     print("-+-+-")
#     print(board["mL"] + "|" + board["mM"] + "|" + board["mR"])
#     print("-+-+-")
#     print(board["lL"] + "|" + board["lM"] + "|" + board["lR"])

# turn = "X"
# for i in range(9):
#     printBoard(theBoard)
#     print("Turn for " + turn + ". Move on which space (tL/mR/lM etc)")
#     move = input()
#     theBoard[move] = turn
#     if turn == "X":
#         turn = "O"
#     else:
#         turn = "X"
# printBoard(theBoard)

# allGuests = {"Alice": {"apples": 5, "pretzels": 12},
#             "Bob": {"ham sandwitches": 3, "apples": 2},
#             "Carol": {"cups": 3, "apple pies": 1}}

# #print(allGuests["Alice"].get("apples"))

# def totalBrought(guests, item):
#     numBrought = 0
#     for k,v in guests.items():
#         print(v.get(item,0))
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought

# print("- Apples " + str(totalBrought(allGuests, "apples")))

# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# def displayInventory(inventory):
#     print('Inventory:')
#     item_total = 0
#     for k, v in inventory.items():
#         print(str(v) + " " + k)
#         item_total += inventory.get(k, 0)
#     print('Total number of items: ' + str(item_total))

#displayInventory(stuff)

#### second part

# def addToInventory(inventory, addedItems):
#     #code
#     for i in addedItems:
#         inv.setdefault(i,0)
#         inv[i] += 1
#     return inv

# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)