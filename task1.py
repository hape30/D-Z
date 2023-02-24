a = int(input())#ввод значений
b = int(input())
c = int(input())
if c<=a:#условие еcли 
    t=2*b #
    print(t) 
elif c*2%a ==0: 
    t=b*(c*2//a)
    print(t) 
else: 
    t=b*(1+(c*2//a))
    print(t) 