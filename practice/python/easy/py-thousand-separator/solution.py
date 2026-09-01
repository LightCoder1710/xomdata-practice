# Xom Data · Show a price in Vietnamese number format
# Problem: https://xomdata.com/practice/py-thousand-separator
# Solved: 2026-09-01

def format_price(amount):
    s = str(amount)
    dai = len(s)
    chen = "."
    i = 3
    
    while i < dai:
        cc = dai - i  # Vị trí cần chèn tính từ đầu chuỗi ban đầu
        # Cắt từ đầu đến cc, chèn dấu chấm, nối với phần còn lại
        s = s[:cc] + chen + s[cc:]
        i += 3
        # Vì vừa chèn thêm 1 ký tự nên tăng độ dài chuỗi thêm 1
        dai += 1
        i += 1  # Bù 1 bước cho ký tự chấm vừa thêm
        
    return s
