# Xom Data · Total receipts
# Problem: https://xomdata.com/practice/py-sum-positive
# Solved: 2026-09-01

def sum_positive(numbers):
    sum = 0
    for num in numbers:
        if num > 0:
            sum = sum + num
    return sum
