# <câu lệnh> 
#  for biến in danh_sach:
#     câu lệnh

# in ra 10 lần màn hình dòng thông báo 'hello world'
for i in range(1,11,1) : # range(giá trị bắt đầu, giá trị kết thúc, bước nhảy)
    print(f'hello world {i}')

# tính tổng các số từ 1 đến n 
n = int(input('nhập n = '))
tong = 0 
for i in range(1, n+1):
    tong = tong + i
print(tong)