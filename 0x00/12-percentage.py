#!/usr/bin/python
"""a module that """

# store score and total marks
score = 45
total = 60

#calculate percentage 
percentage = (score / total ) * 100

# format to two decimal places
message = "Alice scored {:.2f}%" .format(percentage)

print(message) 