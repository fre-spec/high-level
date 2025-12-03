#!/usr/bin/python 
"""a module that calculates the employees bonus """

def calculate_bonus(salary, performance_rating):
    if performance_rating == "Excellent":
        percent = 20
    elif performance_rating == "Good":
        percent = 10
    elif performance_rating == "Average":
        percent = 5
    else:
        return None 
    bonus = salary * (percent / 100)
    return salary + bonus 
if __name__ == "__main__":
    salary = float(input("Enter employee salary: "))
    rating = input("Enter performance rating (Excellent, Good, Average):")

    total = calculate_bonus(salary, rating)

    if total is None:
        print("invalid rating")
    else:
        print("Total salary including bonus:", total)