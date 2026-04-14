a = 'Hello'
b = 'world'
c = '''
        hello1
        hello2
    '''
d = a+b
e = a*5 # không có phép trừ và phép chia
f = 'hello truong'
print(e)

# truy cập tới chỉ số
print(a[1])

# truy cập chỉ số nhiều
print(f[0:5])
#trích xuất từ 6 tới hết 
print(f[6:])
#viết hoa
print(a.upper())
#viết thường
print(a.lower())
#loại bỏ khoảng trắng
print(a.strip())
#số lượng ký tự trong chuỗi
print(len(a))
#thay thế chuỗi
print(f.replace("hello",'good afternoon'))
#tìm ra một từ nào đó
print(f.find("hello")) # ra chỉ số 
# tách toàn bộ ra 1 danh sách
print(a.split())