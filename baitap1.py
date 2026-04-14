# biện luận nghiệm của phương trình ax + b = 0 
# a = b = 0 : vế trái =0 = vế phải => có vô số nghiệm 
# a = 0 và b != 0 : vế trái != 0 => vô nghiệm
# a != 0 và b = 0 : ax =0 => có nghiệm x =0 (duy nhất)
# a và b đều khác 0 : x = -b/a 


a = float(input('a='))
b = float(input('b='))

if a == b == 0 : 
    print('có vô số nghiệm')
elif a == 0 and b != 0: 
    print('vô nghiệm')
elif a!=0 and b==0 : 
    print('x là nghiệm duy nhất')
else: 
    print(f'x = {-b/a}')



# bài 2 : biện luận nghiệm của phương trình ax^2 + bx + c = 0 
import math

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

delta = b**2 - 4*a*c
if delta > 0 : 
    print('có 2 nghiệm phân biệt')
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print(f'giá trị x1 ={x1}')
    print(f'giá trị x2 ={x2}')
elif delta == 0 : 
    print(' có nghiệm kép')
    print(f'x= {-b/(2*a)}')
# delta < 0
# sqrt(delta ) (-1 = i^2) -> sqrt(i^2 * delta)-> i*sqrt(delta) ||| x1 = (-b + sqrt(delta))/(2*a) = -b/(2a) + sqrt(delta)/(2a)
else:
    print('có nghiệm phức')
    print(f'x1={-b/(2*a)} + i*{math.sqrt(abs(delta))/(2*a)}')
    print(f'x2={-b/(2*a)} - i*{math.sqrt(abs(delta))/(2*a)}')

