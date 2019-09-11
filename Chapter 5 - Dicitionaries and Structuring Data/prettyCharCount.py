import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] += 1

pprint.pprint(count)
print()
a = pprint.pformat(count)
print('a element 0:', a[0])
a = list(a)
a.pop(0)
a = '/'.join(a)
print(print('a element 0:', a))

