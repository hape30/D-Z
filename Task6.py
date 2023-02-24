a = float(input())
b = float(input())
c = float(input())
D = (b**2) - ((4 * a * c))
print(D)
if D > 0:
    D **= 0.5
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)
    print(x1, x2)
elif D == 0:
    D **= 0.5
    x = (-b) / (2 * a)
    print(x)
else:
    print("нет корней")