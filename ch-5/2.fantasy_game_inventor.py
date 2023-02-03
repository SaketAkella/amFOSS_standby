stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory: ")
    item_total=0
    for key,value in inventory.items():
        print(value, end=" ")         
        print(key)
        item_total= item_total + int(value)
    print("Total number of items: " +str(item_total))

displayInventory(stuff)