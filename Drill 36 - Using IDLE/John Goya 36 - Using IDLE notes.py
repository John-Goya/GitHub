# -*- coding: cp1252 -*-
'''

    Python:   2.7.13

    Author:   John S. Goya

    Purpose:  Tech Academy Tutorial - #36 - Use IDLE.

        DRILL: 

        Write a program in Python 2.7 using IDLE that demonstrates the following concepts:

        Use comments in your program to denote where you demonstrate each step.
        If there are any concepts you are not able to demonstrate, research them online first.
        If you still have trouble, ask an Instructor for assistance. 

        *1. Assign an integer to a variable
        *2. Assign a string to a variable
        *3. Assign a float to a variable
        *4. Use the print function and .format() notation to print out the variable you assigned  
        5. Use each of these operators
                eg, x = 15, y = 4

            +   print('x + y =',x+y)
                x + y = 19
            
            -   print('x - y =',x-y)
                x - y = 11

            *   print('x * y =',x*y)
                x * y = 60

            /   print('x / y =',x/y)
                x / y = 3.75

            +=  adds a value from variable, setting the variable to the result,
                +=	x += 5	x = x + 5
            =
            % - Modulus, remainder of the division of left operand
                by the right	x % y (remainder of x/y)
                print('x % y =',x%y)
                x % y = 3
            
        6. Use of logical operators:
            and - True if both the operands are true	x and y
            or  - True if either of the operands is true	x or y
            not - True if operand is false (complements the operand) not x
            
                x = True
                y = False

                # Output: x and y is False
                print('x and y is',x and y)
                x and y is False

                # Output: x or y is True
                print('x or y is',x or y)
                x or y is True

                # Output: not x is False
                print('not x is',not x)
                not x is False

            
        7. Use of conditional statements:
            if
            elif
            else

            if, else, elif are used for conditional branching or decision making.

                When we want to test some condition and execute a block only if
                the condition is true, then we use if and elif.
                elif is short for else if.
                else is the block which is executed if the condition is false.
                This will be clear with the following example:

                def if_example(a):
                    if a == 1:
                        print('One')
                    elif a == 2:
                        print('Two')
                    else:
                        print('Something else')

                if_example(2)
                if_example(4)
                if_example(1)
                Output

                Two
                Something else
                One
                Here, the function checks the input number and prints the result if it is 1 or 2.
                Any input other than this will cause the else part of the code to execute.
            
        8. Use of a while loop
        9. Use of a for loop
        10. Create a list and iterate through that list
            using a for loop to print each item out on a new line
        11. Create a tuple and iterate through it
            using a for loop to print each item out on a new line
        12. Define a function that returns a string variable
        13. Call the function you defined above and print the result to the shell
'''
 
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
print name.upper()

# 5. Use each of these operators  +, - , * , / , +=, ­= , %


'''
firstName = raw_input('Enter first name: ')
lastName = raw_input('Enter last name: ')print (firstName).capitalize()+' '+(lastName).capitalize()
'''



x=[]
x += "12345"
print(x)
x -= "45"
print(x)

'''
def start():
    print(get_number())
def get_number():
    number = 12
    return number



if __name__ == "__main__":
    start()
'''
# -*- coding: cp1252 -*-
'''
 
    Python:   2.7.13
 
    Author:   John S. Goya
 
    Purpose:  Tech Academy Tutorial - #36 - Use IDLE.
 
DRILL: 

Write a program in Python 2.7 using IDLE that demonstrates the following concepts:
 
    Use comments in your program to denote where you demonstrate each step.
    If there are any concepts you are not able to demonstrate, research them online first.
    If you still have trouble, ask an Instructor for assistance. 
 
  1. Assign an integer to a variable
  2. Assign a string to a variable
  3. Assign a float to a variable
  4. Use the print function and .format() notation to print out the variable you assigned  
  5. Use each of these operators
     eg, x = 15, y = 4
 
            +   print('x + y =',x+y)
                x + y = 19
            
            -   print('x - y =',x-y)
                x - y = 11
 
            *   print('x * y =',x*y)
                x * y = 60
 
            /   print('x / y =',x/y)
                x / y = 3.75
 
            +=  adds a value from variable, setting the variable to the result,
                +=	x += 5	x = x + 5
            =
            % - Modulus, remainder of the division of left operand
                by the right	x % y (remainder of x/y)
                print('x % y =',x%y)
                x % y = 3
            
6. Use of logical operators:
        There are three logical operators, and, or, and not, that allow us to build more complex Boolean expressions from simpler Boolean expressions.
        The semantics (meaning) of these operators is similar to their meaning in English.
        For example, x > 0 and x < 10 produces True only if x is greater than 0 andat the same time, x is less than 10.
        n % 2 == 0 or n % 3 == 0 is True if either of the conditions is True, that is, if the number n is divisible by 2 or it is divisible by 3. (
            What do you think happens if n is divisible by both 2 and by 3 at the same time? Will the expression yield True or False? Try it in your Python interpreter.)
        Finally, the not operator negates a Boolean value, so not (x > y) is True if (x > y) is False, that is, if xis less than or equal to y.
        The expression on the left of the or operator is evaluated first: if the result is True,
            Python does not (and need not) evaluate the expression on the right — this is called short-circuit evaluation.
        Similarly, for the and operator, if the expression on the left yields False, Python does not evaluate the expression on the right.
        So there are no unnecessary evaluations.
 
 
 
 
        Operation
        Result
        Notes
        x or y
        if x is false, then y, else x
        (1)
        x and y
        if x is false, then x, else y
        (2)
        not x
        if x is false, then True, else False
        (3)
        Notes:
        This is a short-circuit operator, so it only evaluates the second argument if the first one is false.
        This is a short-circuit operator, so it only evaluates the second argument if the first one is true.
        not has a lower priority than non-Boolean operators, so not a== b is interpreted as not (a == b), and a == not b is a syntax error.
________________________________________________________________
 
            and - True if both the operands are true	x and y
            or  - True if either of the operands is true	x or y
            not - True if operand is false (complements the operand) not x
            
                x = True
                y = False
 
                # Output: x and y is False
                print('x and y is',x and y)
                x and y is False
 
                # Output: x or y is True
                print('x or y is',x or y)
                x or y is True
 
                # Output: not x is False
                print('not x is',not x)
                not x is False
 
            
7. Use of conditional statements: pg 22
 
        https://cscircles.cemc.uwaterloo.ca/9-else-and-or-not/	
 
            if
            elif
            else
 
            if, else, elif are used for conditional branching or decision making.
 
                When we want to test some condition and execute a block only if
                the condition is true, then we use if and elif.
                elif is short for else if.
                else is the block which is executed if the condition is false.
                This will be clear with the following example:
 
                def if_example(a):
                    if a == 1:
                        print('One')
                    elif a == 2:
                        print('Two')
                    else:
                        print('Something else')
 
                if_example(2)
                if_example(4)
                if_example(1)
                Output
 
                Two
                Something else
                One
                Here, the function checks the input number and prints the result if it is 1 or 2.
                Any input other than this will cause the else part of the code to execute.
            
8. Use of a while loop
9. Use of a for loop
10. Create a list and iterate through that list
       using a for loop to print each item out on a new line
11. Create a tuple and iterate through it
       using a for loop to print each item out on a new line
12. Define a function that returns a string variable
13. Call the function you defined above and print the result to the shell
'''
 
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
# print (cost + items)
 
# 4. Use the print function and .format() notation to print out the variable you assigned
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
 
 
# 8. Use of a while loop
 
candy_in_bag = 10
while candy_in_bag >= 1:
    print 'Eat one piece of candy! ' + str(candy_in_bag) + ' pieces left!'
    candy_in_bag = candy_in_bag-1
 
 
# 9. Use of a for loop
 
for number in range(1,10):
    if number == 3:
        break
    print number
 
# 10. Create a list and iterate through that list using a for loop to print each item out on a new line
 
days_of_the_week=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for days in days_of_the_week:
    print days
 
# 11. Create a tuple and iterate through it using a for loop to print each item out on a new line
 
days_of_the_week=('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
for days in days_of_the_week:
    print days
 
 
# 12. Define a function that returns a string variable
 
def stayorgo(traffic_light_color):
    if traffic_light_color == 'red':
        print ('Hit the brakes!')
    elif traffic_light_color =='yellow':
        print ('Slow down before the traffic light!')
    else:
        print ('Proceed through the intersection with caution!')
 
 
 
 
 
# 13. Call the function you defined above and print the result to the shell
 
print stayorgo('red')
 
 
 
 
