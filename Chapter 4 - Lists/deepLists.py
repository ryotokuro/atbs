import copy

originalList = ['come', 42, 19.8]

referenceList = originalList
referenceList[1] = 'directChange'

print(originalList)

deepList = ['deeper', 88, 'rising']
referenceList[2] = [deepList]

modifyList = deepList

copyList = copy.deepcopy(originalList)
copyList[2] = 'removed the deepList'

print(originalList)
print(copyList)