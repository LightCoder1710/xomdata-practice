# Xom Data · Add up the day's slip numbers
# Problem: https://xomdata.com/practice/py-sum-to-n
# Solved: 2026-09-01

def sum_to(n):
    i = 0
    sum = 0
    while i <= n:
        sum += i
        i+=1
    return sum
