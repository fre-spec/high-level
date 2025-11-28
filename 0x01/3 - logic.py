#!/usr/bin/python 
"""a module that """
score = int(input("Enter your score:"))

if score  >= 90 and score  <= 100:
    print(" grade A")
elif score >= 80 and score <=89:
    print("grade B")
elif score >= 70 and score <= 79:
    print("grade C")
elif score >= 60 and score <= 69:
    print("grade D")
elif score >= 0 and score <= 59:
    print("grade F")
else :
    print("invalid score")