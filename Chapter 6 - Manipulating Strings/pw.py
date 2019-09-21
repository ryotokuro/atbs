#! python3
# pw.py - An insecure password locker program

passwords = {
    'email':'3fnFAG2rgSV5ggnSxxbuDDvnis',
    'blog':'WALM93t98nXCVsVv2DVvfvfvd',
    'luggage':'47882'
     }

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name
print(account)
