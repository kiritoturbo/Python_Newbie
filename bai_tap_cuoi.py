# bai1: nhập vào 3 số a,b,c. Tính và in ra d = (a+b)^c. Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
a = float(input('Nhập vào a = '))
b = float(input('Nhập vào b = '))
c = float(input('Nhập vào c = '))

d = (a+b)**c
if 100 <= d <= 200: 
    print(f'True {d}')
else:
    print(f'False {d}')


# bài 2: Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b 
a = int(input("a="))
b = int(input("b="))
uoc_chung=[]
if a > b:
    for i in range(1,b+1):
        if a % i == 0 and b % i == 0 : 
            uoc_chung.append(i)
print(uoc_chung)

# bài 3: Nhập vào một số nguyên dương n , kiểm tra xem n có phải là số dạng 2^k hay không ( k là nguyên dương)
# k = 0 --> 2^0 so sánh với n : nhỏ hơn n thì tăng số mũ đến khi : bằng n thì có dạng 2^k, lớn hơn n thì có dạng 2^k 
n = int(input('n='))
i = 0 
k=0
h= 2**i 
while h<n:
    i+=1
    k+=1
    h=2**i 
if h==n:
    print(f'có dạng 2^{k}')
else:
    print('không có dạng 2^k')
    #và cho biết k bằng bao nhiêu

# bài 4: viết ham đưa vào 1 số nguyên a, kiểm tra xem a có phải là một số Armstrong hay không 
# 123: 3 chữ số : nếu 1^3 + 2^3 + 3^3 = 123 thì 123 là số amstrong 
def baitap4(n):
    so = str(n)
    dai= len(so)
    tong = 0
    for i in so:
        tong = tong + int(i)**dai
    print('Là số Armstrong') if tong == n else print('không là số armstrong ')
baitap4(153)