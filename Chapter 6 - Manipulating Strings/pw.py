#! python3
# pw.py - An insecure password locker program
import sys, pyperclip

passwords = {
    'email':'3fnFAG2rgSV5ggnSxxbuDDvnis',
    'blog':'WALM93t98nXCVsVv2DVvfvfvd',
    'luggage':'47882'
     }

# if no command-line argument was entered
if len(sys.argv) < 2:  # error
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()  # and close the program

account = sys.argv[1]  # first command line arg is the account name
print(account)

if account not in passwords:
    print('There is no account:', account)
else:
    pyperclip.copy(passwords[account])
    print('Password for', account, 'copied to clipboard.')

    # visual box
    import tkinter as tk 

    root= tk.Tk() 
    #canvas1 = tk.Canvas(root, width = 300, height = 300)
    button1 = tk.Button (root, text='user:' + account, command=root.destroy)
    button2 = tk.Button (root, text='pass:' + passwords[account], command=root.destroy)
    button1.pack()
    button2.pack()
    #canvas1.pack
    #canvas1.create_window(150, 150) 
    root.mainloop()
