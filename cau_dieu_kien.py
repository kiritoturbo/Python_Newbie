# nhập vào 1 số nguyên và kiểm tra số đó là số chẵn hay lẻ 
a = int(input('nhập a='))
if a % 2 ==0 and a != 0:
        print('số chẵn')
elif a % 2 != 0: 
    print('số lẻ')
else : 
    print('số 0')


# bài 2: nhập vào 3 số thực dương a, b, c . Kiểm tra xem a,b,c có cấu thành 1 tam giác được không 
a = float(input('Nhập số thực dương a ='))
b = float(input('Nhập số thực dương b ='))
c = float(input('Nhập số thực dương c ='))
if( a < 0 or b < 0 or c < 0 ):
    print("nhập lại số dương")
    a = float(input('Nhập số thực dương a ='))
    b = float(input('Nhập số thực dương b ='))
    c = float(input('Nhập số thực dương c ='))

if a + b > c and b + c > a and a+c>b :
     print('Tạo thành một tam giác')
else:
     print('Không tạo thành một tam giác')
