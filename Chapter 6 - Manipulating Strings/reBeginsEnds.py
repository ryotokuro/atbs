import re

# begins
begins_with = re.compile(r'^Location:')
begins = begins_with.search('Location: 32.2')

# ends
ends_with = re.compile(r'\D{7}$')
ends = ends_with.search("For example, the r'^Hello' regular expression string matches strings that begin with 'Hello'")

print(begins)
