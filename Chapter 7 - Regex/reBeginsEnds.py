import re

# begins
begins_with = re.compile(r'^Location:')
begins = begins_with.search('Location: 32.2')
print(begins.group())

# ends
ends_with = re.compile(r'\D+$')
ends = ends_with.search("For example, the r'^Hello' regular expression string matches strings that begin with 'Hello'")
print(ends.group())

# starts and ends
numbers_only = re.compile(r'^\d+$')
numbers = numbers_only.search('71843')
print(numbers.group())
numbers = numbers_only.search('34 23')
print(numbers)


