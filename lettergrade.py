'''
Program: lettergrade.py
Author: Elayna Ridley
Course: CSC 111L, Lab 4
Purpose: To print out the letter grade that corresponds to the input number grade.
'''

grade = float(input('What is the student grade? (0-100) ? '))

if grade >= 93.0:
    score = 'A'
elif grade >=90:
    score = 'A-'
elif grade >= 87:
    score = 'B+'
elif grade >= 83:
    score = 'B'
elif grade >= 80:
    score = 'B-'
elif grade >= 75:
    score = 'C+'
elif grade >= 70:
    score = 'C'
elif grade >= 65:
    score = 'C-'
elif grade >= 55:
    score = 'D'
else:
    score = 'F'

print('The letter grade is', score)
