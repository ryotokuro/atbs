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

import tkinter as tk 

root= tk.Tk() 
   
canvas1 = tk.Canvas(root, width = 300, height = 300) 
canvas1.pack()
      
button1 = tk.Button (root, text='pw:' + sys.argv[1], command=root.destroy) 
canvas1.create_window(150, 150, window=button1) 
    
root.mainloop()
