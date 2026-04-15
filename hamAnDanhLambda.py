m = lambda a,b:a+b # hàm ẩn danh , ko có tên gì 
print(m(1,2))
# map() áp dụng một hàm cho một phần tử
L = [1,2,3,4,5]
kq = list(map(lambda x:x**2,L))
print(kq)

#filter() lọc phần tử thỏa mãn điều kiện
L = [1,2,3,4,5,8,9,6,2,1]
kq = list(filter(lambda x:x%2==0 and x !=0,L))
print(kq)

#sorted() sắp xếp với key
ten = ['an','truong','ngoc','huyen','trung','chi','yen']
kq=sorted(ten,key=lambda x:len(x))
print(kq)

#reduce() - tích lũy giá trị
from functools import reduce
L = ['1','2','3','34']
kq = reduce(lambda x,y: int(x) + int(y),L)
print(int(kq))