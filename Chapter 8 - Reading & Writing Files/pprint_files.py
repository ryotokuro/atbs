# previously I named my file pprint, so it was having trouble finding a p.format
# attribute!!! so lesson learned, never name the same as imports

import pprint as p

cats = [{'name': 'Sophie', 'desc': 'chubby'}, {'name': 'Gnar', 'desc': 'fluffy'}]
print(p.pformat(cats))


fileObj = open('myCats.py', 'w')
# pformat is like format() in Java
fileObj.write('cats = ' + p.pformat(cats) + '\n')
fileObj.close()
