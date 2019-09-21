def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':9001}
printPicnic(picnicItems, 10, 5)
inventory = {'rope':7, 'potions':4, 'weapons':2, 'food':16}
printPicnic(inventory, 30, 2)
