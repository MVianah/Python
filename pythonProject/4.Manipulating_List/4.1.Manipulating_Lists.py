vList = ['Matheus', 'Gabriel']

# append()
vList.append('Benjamim')
print('append() -> ' + str(vList))

# len()
print('len() -> ', len(vList))

# []
print('[ ] -> ', vList[1])

# insert()
vList.insert(1,'João')
print('insert() -> ', vList)

# extend()
vList_01 = ['Gabriel', 'Matheus']
vList_02 = ['Benjamim', 'Armira']

vList_01.extend(vList_02)
print('extend() -> ', vList_01)

# remove()
vList.remove('Gabriel')
print('remove() -> ', vList)

# pop
vList.pop(0)
print('pop() -> ', vList)

# sort()
vList_Text = ['d', 'a', 'f', 'e', 'c', 'b']
vList_Text.sort()
print('sort() -> ', vList_Text)

# copy()
vList_Copy = vList_Text.copy()
print('copy() -> ', vList_Copy)
