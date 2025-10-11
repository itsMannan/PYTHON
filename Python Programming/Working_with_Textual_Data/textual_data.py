message = "Hello World"

print(message)

message2 = "Bobby's World"
print(message2)


message3 = 'Bobby\'s World'
print(message3)

message4 = """I'm doing the practise
of python from \"Corey Schafer\" channel on 
youtube"""
print(message4)

message5='Hello World'
print(len(message5)) # To check the characters of our strings
 
message6 = "Hello World"
print(message6[0])

message7 = "Hello World"
print(message7[10])

#Slicing Technique
message8 = "Hello World"
print(message8[0:5]) # add value from 0 include 0 too upto 5-1 mean index 4 excluding the 5th index 


message9 = "Hello World"
print(message9[:5])

message10 = "Hello World"
print(message10[6:])


message11 = "Hello World"
print(message11.lower())

message12 = "Hello World"
print(message12.upper())
  
message13 = "Hello World"
print(message13.count('l'))

message14 = "Hello World"
print(message14.count('Hello'))


message15 = "Hello World"
print(message15.find('World'))

message16 = "Hello World"
print(message16.find('universe'))

message17 = "Hello World"
print(message17.replace('World' , 'Universe'))

message18 = "Hello World"
message18 = message18.replace('World','universe')
print(message18) 

greeting = "Hello"
name = "Abdul Mannan"
message19 = greeting + ', ' + name 
print(message19)


greeting = "Hello"
name = "Abdul Mannan"
message20 = greeting + ', ' + name  + '. Welcome:'
print(message20)

greeting = "Hello"
name = "Abdul Mannan"
message21 = '{} , {}, Welcome!'.format(greeting , name)
print(message21)

#f-strings
greeting = "Hello"
name = "Abdul Mannan"
message22 = f'{greeting} , {name.upper()}, Welcome!'
print(message22)

greeting = "Hello"
name = "Abdul Mannan"
# message22 = '{} , {}, Welcome!'.format(greeting , name)
print(dir(name))


greeting = "Hello"
name = "Abdul Mannan"
# message22 = '{} , {}, Welcome!'.format(greeting , name)
print(help(str))

greeting = "Hello"
name = "Abdul Mannan"
# message22 = '{} , {}, Welcome!'.format(greeting , name)
print(help(str.lower)) 