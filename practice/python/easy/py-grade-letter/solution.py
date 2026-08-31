# Xom Data · Letter grade from score
# Problem: https://xomdata.com/practice/py-grade-letter
# Solved: 2026-08-31

def grade_letter(score):
    if score <= 100 and score >= 0:
        if score >= 90:
            return "A"
        elif score >= 80 and score< 90:
            return "B"
        elif score >= 70 and score< 80:
            return "C"
        elif score >= 60 and score< 70:
            return "D"
        else:
            return "F"
    else: 
        pass
