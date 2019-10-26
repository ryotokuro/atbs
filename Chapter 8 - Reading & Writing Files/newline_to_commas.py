import pyperclip as py

string = py.paste()
string = string.replace("\n", ", ")
string = string.strip(" ")

py.copy(string)
