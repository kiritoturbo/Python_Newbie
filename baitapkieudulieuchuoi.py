#nhập vào một chuỗi bất kỳ và phân loại ký tự trong chuỗi đó
# ký tự số: 12,3,4,./..
# ký tự hoa: H, M, N...
# ký tự thường: m, l, k....
# ký tự đặc biệt:/,?
a = input('nhập vào chuỗi của bạn: ')

so = ''
chuHoa =''
chuThuong =''
chuDacbiet =''
for i in a : 
    if i.isdigit(): #kiểm tra xem có phải số không
        so = so + ',' + i
    elif i.isupper():#kiểm tra xem có phải chữ hoa ko
        chuHoa = chuHoa + ','+ i
    elif i.islower():
        chuThuong = chuThuong + ','+ i
    else: 
        chuDacbiet = chuDacbiet + ','+i 
print(f'Các ký tự số có trong chuỗi là {so}')
print(f'Các ký tự chữ Hoa có trong chuỗi là {chuHoa}')
print(f'Các ký tự chữ thường có trong chuỗi là {chuThuong}')
print(f'Các ký tự chữ đặc biệt có trong chuỗi là {chuDacbiet}')



'''
kiểm tra độ khỏe của mật khẩu: 
nếu mật khẩu có đủ các yếu tố sau thì coi là mật khẩu khỏe 
 só số lượng ký tự lớn hơn hoặc bằng 8 
 có ít nhất 1 ký tự hoa , 1 ký tự thường, 1 ký tự số và 1 ký tự đặc biệt
'''
so = 0
chuHoa =0
chuThuong =0
chuDacbiet =0
for i in a : 
    if i.isdigit(): #kiểm tra xem có phải số không
        so = so + 1
    elif i.isupper():
        chuHoa = chuHoa + 1
    elif i.islower():
        chuThuong = chuThuong + 1
    else: 
        chuDacbiet = chuDacbiet + 1


if len(a) > 8 and so >=1 and chuHoa >=1 and chuThuong >=1 and chuDacbiet >=1: 
    print('mật khẩu khỏe')
else:
    print('Yếuu')



# bài 3: nhậ vào 1 chuỗi, hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng
b = input('nhập chuỗi: ')
tong = 0 
for i in b:
    if i.isdigit():
        print(i)
        tong = tong + int(i)
print(tong)


# bài 4 : nhập vào một chuỗi, hãy tách toàn bộ con số trong chuỗi ra rồi tính tổng của chúng ( ví dụ 2 số đứng cạnh nhau thì được coi là một số)
# ví dụ  : abd45ecf47wde3s1
c = input('nhập chuỗi c: ')
tong = 0 
so = ''
c = c + ' ' 
for i in c:
    if i.isdigit():
        so = so + i
    else: 
        if so != '':
            tong = tong + int(so)
            so = ''
print(tong)