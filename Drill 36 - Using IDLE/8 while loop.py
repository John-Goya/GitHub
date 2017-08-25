# -*- coding: cp1252 -*-

# 1. Assign an integer to a variable
items = 5
print ('#1 Assign an integer to a variable (now string in this line, integer output on next line)= ' + str(items))
print items

print ('\n# 2. Assign a string to a variable')
name = 'john goya'
print name

print ('\n# 3. Assign a float to a variable')
cost = 1.50
print cost
print (cost + items)

print ('\n# 4. Use the print function and .format() notation to print out the variable you assigned')
print name.upper()

print ('\n# 5. Use each of these operators  +, - , * , / , +=, ­= , %')
print ('variables:\nx = 11\ny = 2')
x = 11
y = 2

# +
print ('\nx+y')
print x+y

# -
print ('\nx-y')
print x-y
 
# *
print ('\nx*y')
print  x*y
 
# /
print ('\nx/y')
print x/y


# x += y
print ('\nx += y')
x += 3
print x


# =
print ('\nx=y')
x=y
print y


# %
print ('\nvariables:\nx = 8\ny = 3')
x = 8
y = 3
print ('x%y')
print x%y

print ('\n#6 Use of logical operators: and, or, not')
       
x = 20
y = 30
 
if x > 10 and y > 10:
  print('both x AND y are true!')
 
 
if x > 25 or y > 25:
  print('x OR y IS true!')
 
if not y > 40:
  print('NOT true!')

print ('\n# 7. Use of conditional statements: if, elif, else')
 
minutes_of_fame=1
 
if minutes_of_fame < 15:
	print('On the road to glory!')
elif minutes_of_fame == 15:
	print('I’m king of the world!')
else:
	print('There goes the glory!')

print ('\n#8. Use of a while loop')
candy_in_bag = 10
while candy_in_bag >= 1:
    print 'Eat one piece of candy! ' + str(candy_in_bag) + ' pieces left!'
    candy_in_bag = candy_in_bag-1

print ('\n#9. Use of a for loop')
days_of_the_week=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for days in days_of_the_week:
    print days,
print ('\n')
print ('\n#10. Create a list and iterate through that list using a for loop to print each item out on a new line')
days_of_the_week=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for days in days_of_the_week:
    print days

print ('\n11. Create a tuple and iterate through it using a for loop to print each item out on a new line')
traffic_light_color=('red', 'yellow', 'green');
actions_for_driver=('stop','slowdown','go');
length_of_time=(30,5,30)
for colors in traffic_light_color:
    print colors
for action in actions_for_driver:
    print action
for time in length_of_time:
    print time



print ('\n12. Define a function that returns a string variable')
def stayorgo(traffic_light_color):
    if traffic_light_color == 'red':
        print ('Hit the brakes!')
    elif traffic_light_color =='yellow':
        print ('Slow down before the traffic light!')
    else:
        print ('Proceed through the intersection with caution!')

print ('\n13. Call the function you defined above and print the result to the shell')
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

for number in range(1,10):
    if number == 3:
        break
    print number
'''

