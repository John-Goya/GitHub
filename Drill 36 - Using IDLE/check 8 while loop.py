# -*- coding: cp1252 -*-

# 1. Assign an integer to a variable
items = 5
print ('#1 Assign an integer to a variable (now string in this line, integer output on next line)= ' + str(items))
print items
 
# 2. Assign a string to a variable
name = 'john goya'
print name
 
# 3. Assign a float to a variable
cost = 1.50
print cost
print (cost + items)
 
# 4. Use the print function and .format() notation to print out the variable you assigned
name = 'john goya'
name.upper()

# 5. Use each of these operators  +, - , * , / , +=, ­= , %
 
# +
x = 11
y = 2
print (x+y)
 
# - 
print (x-y)
 
# *
print  (x*y)
 
# /
print (x/y)
 
# +=
print (x)

# x += y
print (x)
 
# =
print (x)
# x = y
print (x)
 
# %
x = 8
y = 3
print (x%y)

#6 Use of logical operators: and, or, not
       
x = 20
y = 30
 
if x > 10 and y > 10:
  print('both x AND y are true!')
 
 
if x > 25 or y > 25:
  print('x OR y IS true!')
 
if not y > 40:
  print('NOT true!')

# 7. Use of conditional statements: if, elif, else
 
minutes_of_fame=1
 
if minutes_of_fame < 15:
	print('On the road to glory!')
elif minutes_of_fame == 15:
	print('I’m king of the world!')
else:
	print('There goes the glory!')

#8
candy_in_bag = 10
while candy_in_bag >= 1:
    print 'Eat one piece of candy! ' + str(candy_in_bag) + ' pieces left!'
    candy_in_bag = candy_in_bag-1

#9
days_of_the_week=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for days in days_of_the_week:
    print days,

#10
days_of_the_week=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for days in days_of_the_week:
    print days


for number in range(1,10):
    if number == 3:
        break
    print number



def stayorgo(traffic_light_color):
    if traffic_light_color == 'red':
        print ('Hit the brakes!')
    elif traffic_light_color =='yellow':
        print ('Slow down before the traffic light!')
    else:
        print ('Proceed through the intersection with caution!')

print stayorgo('red')


'''
i = 4 
while i < 9:
    print(i)
    i = i+2

# -*- coding: cp1252 -*-
candy_in_bag = 10
while candy_in_bag > 1:
    print ('Eat one piece of candy!')
candy_in_bag = candy_in_bag-1
'''
