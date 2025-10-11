nums = [1 ,2 ,3 ,4 ,5]

for index, num in enumerate(nums , start=1):
    print(index , num)
print('\n')
    
# Two important keywords when working with Loops
# 1 break
# 2 continue

# break
nums = [1 ,2 ,3 ,4 ,5]

for num in nums:
    if num == 4 :
        print('Loops Terminated at reaching 4' )
        break
    else:
        print(num)

print('\n')

# continue
nums = [1 ,2 ,3 ,4 ,5]

for num in nums:
    if num == 4 :
        print('Skiped the number' , num , 'from the loop')
        continue
    else:
        print(num)

print('\n')

# Loop within a loop

nums = [1 ,2 ,3 ,4 ,5]

for num in nums:
    for letter in 'abc':
        print(num , letter , '\n')
        
print('\n')

for i in range(10):
    print(i)

print('\n')  
  
for i in range(1 , 11):
    print(i)
    
print('\n')
# While loops
# While loop keep going until certain condition is met or we add break in it

x = 0
while x < 10:
    print(x)
    x = x + 1 # incrementing we can also increment using { x += 1 }
 
print('\n') 
    
x = 0 
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
    
print('\n')


# infinite loop

x = 0 
while True:
    # if x == 5:
    #     break ( it is must to use break in infinite loop)
    print(x)
    x += 1
     