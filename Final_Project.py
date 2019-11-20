#Name:          Shazam Zafar
#Date:          December 7, 2018
#Class:         Python (Final Project)

import time

#Function for showing data from file
def showDataFromFile():
    with open('imsDB.txt', 'r') as items:
        for item in items:
            print(item,end='')

#Function for finding items in file 
def findItemByName(myitem):
    with open('imsDB.txt', 'r') as items:
        for num, line in enumerate(items, 0):
            if myitem in line:
                return num,line
 
 #append to the file
def addNewItemToFile(currentData):
    items = open("imsDB.txt","a+")
    items.write('\n')
    items.write(currentData)
    items.close()
 
#rewrite the whole file
def updatePreviousItemToFile(index, currentData):  
    with open('imsDB.txt', 'r') as file:
        data = file.readlines()
    data[index] = currentData + '\n'
    with open('imsDB.txt', 'w') as file:
        file.writelines( data )

 #Menu for the program
def menuDisplay():
    print ('=============================')
    print ('= Inventory Management Menu =')
    print ('=============================')
    print ('(1) Add New Item to Inventory')
    print ('(2) Remove Item from Inventory')
    print ('(3) Update Inventory')
    print ('(4) Search Item in Inventory')
    print ('(5) Print Inventory Report')
    print ('(99) Quit')
    try:
        CHOICE = int(input("Enter choice: "))
    except:
        print("Please enter numeric")
        time.sleep(1)
        menuDisplay()
    menuSelection(CHOICE)

#Function and if statment for the choice 
def menuSelection(CHOICE):
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        updateInventory()
    elif CHOICE == 4:
        searchInventory()
    elif CHOICE == 5:
        printInventory()
    elif CHOICE == 99:
        exit()
    else:
        print('Enter valid menu option!!')
        time.sleep(1)
        menuDisplay()
        
 #Showing end menu
def showEndMenu():
    try:
        CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
        if CHOICE == 98:
            menuDisplay()
        else:
            exit()
    except:
        print('Exiting program!!')

#Adding items in to the inventory   
def addInventory():
    print ('Adding Inventory')
    print ('-----------------')
    item = input('Enter the name of the item: ')
    qty = int(input("Enter the quantity of the item: "))
    newItem = item+' : '+str(qty)
    addNewItemToFile(newItem)
    showEndMenu()

 #Removing items from inventory
def removeInventory():
    print ('Removing Inventory')
    print ('-----------------')
    myitem = input("Enter the item name to remove from inventory: ")
    myitem = myitem.strip()
    try:
        index,line = findItemByName(myitem)
        updatePreviousItemToFile(index,'')
    except:
        print('Cannot remove!!')
    showEndMenu()

 #Updating items from the inventory
def updateInventory():
    print ('Updating Inventory')
    print ('-----------------')
    myitem = input('Enter the item to update: ')
    myitem = myitem.strip()
    myqty = int(input("Enter the updated quantity. Enter 5 for additional or -5 for less: "))
    try:
        index,line = findItemByName(myitem)
        lines = line.split(':')
        newqty = int(lines[1].strip()) + myqty
        newline = lines[0].strip() + ' : ' + str(newqty)
        updatePreviousItemToFile(index,newline)
    except:
        print('Cannot update!!')
    showEndMenu()
    
 #Searching the items in the inventory
def searchInventory():
    print ('Searching Inventory')
    print ('-----------------')
    myitem = input('Enter the name of the item: ')
    myitem = myitem.strip()
    try:
        index,line = findItemByName(myitem)
        lines = line.split(':')
        print("Items: ",lines[0].strip())
        print("Quantity: ",lines[1].strip())
    except:
        print("Item not found!!")
    showEndMenu()

 #Printing all the inventory items
def printInventory():
    print ('Current Inventory')
    print ('-----------------')
    showDataFromFile()
    print()
    print ('-----------------')
    showEndMenu()

 #Calling the menu functions
menuDisplay()
