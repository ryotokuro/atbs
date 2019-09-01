def eggs(parameter):
    try:
        parameter.append('Hello')
        parameter[0] = 'Not'
    except AttributeError:
        return None
    
l = [['World', 'Elite'], ['Gone']]
eggs(l)
eggs(1)
print(l)
