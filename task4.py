#входные данные
X = int(input())

#сложение 
part1 = ''
part2 = ''
part3 = ''
count = 0

#вычесляем (сколько L)
if X >= 50 and X < 90:
    part1 = 'L'
    count += 1
elif (X-X%10) == 40:
    part1 = 'XL'

#вычесляем (сколько Х)
if X - count*50 >= 10 and X //10 != 4 and X<90:
    part2 = 'X'*((X - count*50)//10)

#вычисляем (сколько I и V)
if X%10 == 9:
    part3 = 'IX'
elif X%10 >= 5:
    part3 = 'V' + 'I'*(X%10-5)
elif X%10 == 4:
    part3 = 'I'+'V'
else:
    part3 = 'I'*(X%10)


if X == 100:
    print('C')
elif X >=90:
    print('XC'+ part2 + part3)
else:
    print(part1 + part2 + part3)