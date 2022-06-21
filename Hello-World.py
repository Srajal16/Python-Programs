#Print Hello World
message = "Hell\'o World"
m = """Hello my name is 
srajal sawner"""
print(len(message))
print(message[10])
print(message[0:6])
print(m)
print(message.lower())
print(message.count('H'))
print(message.find('World'))
r = message.replace('World','Universe')
print(r)
print(message)
a = 'Hello'
name = 'Srajal'

abc = a + ' , ' + name + '  Welcome! '
message = '{},{} . Welcome!'.format(a,name) #Or This 
#FString 
message = f'{a},{name.upper()}.Welcome!'
print(abc)
print(message)
print(dir(name)) #all methods 
print(help(str.lower))

