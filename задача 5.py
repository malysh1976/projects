x=input('введите строку 1 ')
y=input('введите строку 2 ')
z=input('введите строку 3 ')
x1=len(x)
x2=len(y)
x3=len(z)
max=max(x1,x2,x3)
min=min(x1,x2,x3)
medium=(x1+x2+x3)-max-min
if max-medium==medium-min:
    print("можно")
else:
    print('нельзя')