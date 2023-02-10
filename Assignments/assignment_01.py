#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95


# Get the test scores.
## Since the input function returns strings we will convert them to integers that can actually be calculated with early on through calling int().
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))

## The logical error of computing the average for three tests while only asking the user for two tests can be fixed by asking for the third one below.
test3 = int(input('Enter the score for test 3: '))

# Calculate the average test score.
## Parenthesis have been added to divide the sum of all the test scores by 3 rather than just test 3.
average = (test1 + test2 + test3) / 3

# Print the average.
## The comma was removed as the print function only takes one argument. To print out a cocentated sentence we must cocantetate the variable average that was previously an int and turn it into a string.
print('The average score is ' + str(average))
# If the average is a high score,
# congratulate the user.
## Capitalized HIGH_SCORE because variable names are case sensitive. Also expressions must be kept within the indentation of a condition, so tabbed in the second print() statement.
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')


#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
length1 = int(input('Enter the length for rectangle 1: '))
width1 = int(input('Enter the width for rectangle 1: '))

length2 = int(input('Enter the length for rectangle 2: '))
width2 = int(input('Enter the width for rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2

## Probably what you wanted: print("The area of rectangle 1 is " + str(area1) + " and the area of rectangle 2 is  " + str(area2))
print(f"The area of rectangle 1 is {area1} and the area of rectangle 2 is {area2}")

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.
name = input('Please enter your name:')
age = int(input('Please enter your age:'))

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
## Probably what you wanted: print("Happy birthday, " + name + " ! You are " + str(age) " years old today!")
print(f"Happy birthday, {name}! You are {age} years old today!")