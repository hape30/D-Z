a = int(input())
b = a % 60
if b >= 36: #условие еcли 
    t = a // 60 + 1
    a = 0
    m = 0
else:
    t = a // 60
    if (b % 10) >= 9:
        a = b // 10 + 1
        m = 0
    else:
        a = b // 10
        m = b % 10
print(m, a ,t)