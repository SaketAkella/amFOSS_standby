stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory: ")
    
    item_total=0
    for key,value in inventory.items():
        print(value, end=" ")         
        print(key)
        item_total= item_total + int(value)
        
    print("Total number of items: " +str(item_total))
    
'''   
def addToInventory(inventory, addedItems):
    for i in range (len(dragonLoot)):
        if dragonLoot[i] in inventory:
            inventory[dragonLoot[i]]=inventory[dragonLoot[i]]+1
        else:
            inventory.setdefault(dragonLoot[i])
        
    inv = {'gold coin': 42, 'rope': 1}
 '''

def addToInventory(inventory, addedItems):
    for i in addedItems:
        for k, v in inventory.copy().items():  
            if k == i:
                inventory[k] = v + 1
            if i not in inventory.keys():
                inventory[i] = 1
                    
    return inventory
    '''
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)
addToInventory(inv) 
'''
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(stuff)     