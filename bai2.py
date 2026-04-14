# nhập vào 3 số thực a,b,c : 
# kiểm tra xem 3 số đó có thể tạo thành tam giác được không, nếu có thì hãy tính chu vi , diện tích và cho biết đó là tam giác gì
a = float(input('nhập a='))
b = float(input('nhập b='))
c = float(input('nhập c='))
import math as m # đặt tên bí danh
if a + b > c and b + c > a and a + c > b: 
    print('tạo thành 1 tam giác')
    chuvi = a + b + c #tính chu vi
    p = chuvi/2 # tính nửa chu vi
    s = m.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f'chu vi là {chuvi}')
    print(f'diện tích là {s}')
    k=h=m=0
    # tam giác cân , vuông cân , đều , vuông, thường(nhọn, tù)
    if a==b or a ==c or b ==c :
        # print('tam giác đều') if a ==b ==c else print('tam giác cân')
        print('tam giác cân')
        k=1
    if a ==b ==c : 
        print('tam giác đều')
        h=1
    if a*a == b**b + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('tam giác vuông cân') if a==b or b==c or c==a else print('tam giác vuông')
        m=1
    if(k !=1 and h != 1 and m != 1):
        print('tam giác thường')
else: 
    print('không phải tam giác')