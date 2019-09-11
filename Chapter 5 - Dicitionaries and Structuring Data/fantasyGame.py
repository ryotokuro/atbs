def displayInventory(inventory):
    total_items = 0
    print('Inventory: ')
    for k, v in inventory.items():
        print(v, k)
        # coins don't count as items...
        if k != 'gold coin':
            total_items += v
    print('Total number of items:', total_items)

def addToInventory(loot):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)
print()
print('THE NEXT DAY')
print('Dragon slain! More loot collected.')
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print()
addToInventory(dragonLoot)
displayInventory(inventory)


