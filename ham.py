#def 
# def ten_ham(tham_so_1,tham_so_2,...):
#     #khối lệnh
#     return gia_tri

# viết hàm nhập vào ten người và in ra 'hello{tên người}

def outputname(nameHuman): #definition
    print(f'tên của người này là {nameHuman}')
    return

nhap_tu_ban_phim = input('Nhập tên của ban:')
outputname(nhap_tu_ban_phim)


# bài 2: viết hàm đưa vào 2 số nguyên , số nào lớn hơn thì in bảng cửu chương của số đó
def so_nguyen(a,b):
    if a>b :
        for i in range(1,10):
            print(f'{a} * {i} = {a*i}')
    elif a<b:
        for i in range(1,10):
            print(f'{b} * {i} = {b*i}')
    else:
        print('2 số bằng nhau in cái nào cũng được')
        for i in range(1,10):
            print(f'{b} * {i} = {b*i}')
so_nguyen(3,5)

# bài 3: viết hàm đưa vào 1 list có các phần tử là chuỗi, tìm và trả về chuỗi ngắn nhất trong list 
L = ['xin', 'hi', 'chào','hello']
def bai3(L):
    l_tam =[]
    for i in L : 
        l_tam.append(len(i))
    kq = l_tam.index(min(l_tam))
    return L[kq]

print(bai3(L))
    