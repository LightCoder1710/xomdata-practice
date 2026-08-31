# Xom Data · Compute price after discount
# Problem: https://xomdata.com/practice/py-discount
# Solved: 2026-08-31

def final_price(price, percent):
    percent = percent/100
    realprice = price - (price * percent)
    return realprice
