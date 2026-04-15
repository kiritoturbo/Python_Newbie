# list 
L = [1,5,2,3,6,4,7] #list số
L1 = [8,9,10]
# gọi 1 phần tử 
print(L[2])
print(L+L1)
# thay đổi số trong chuỗi
L[1]=10
print(L)
#phép nhân list
print(L*5)
#lấy ra 1 khúc nào đó trong list 
print(L[1:4])
# hàm có sẵn 
# thêm cái gì vào cuối cùng
L.append(11)# thêm một list khác hoặc bất cứ dữ liệu vào 

#thêm vị trí bất kì
L.insert(1,100)#(vị trí index, giá trị sẽ thay thế)
# xóa đi
L.remove(1)
#tính số lượng phần tử 
print(len(L))
#tính tổng các phần tử 
print(sum(L))
# sắp xếp tăng dần
print(sorted(L))# sorted không biến đổi list ban đầu 
L.sort() # thay đổi list ban đầu 
# in ra giá trị lớn nhất, nhỏ nhất
print(min(L))
print(max(L))


# bài tập : in ra màn hình list các phần tử là các số chính phương trong khoảng từ 1 đến 100    
L = [x**2 for x in range(1,11)]
print(L)
# cách khác
L = []
for x in range(1,11):
    L.append(x**2)

print(L)


