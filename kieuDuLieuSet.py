# set là một kiểu dữ liệu được dùng để lưu trữ tập hợp các phần từ không trùng lặp. Đây là một kiểu dữ liệu khong có thứ tự và không cho phép chứa các phần từ lặp lại 
# kiểu set thì các giá trị sắp xếp từ bé tới lớn 
# được giá trị đơn lẻ nhưng lại là ngoặc nhọn như kiểu dữ liệu từ điển chứ ko phải key: value
# không hỗ trợ truy cập phần tử từ chỉ số index
# chỉ truyền 1 kiểu dữ liệu 

k_set = set([1,2,5,4,3,7,8,9,5,6,44,59,62])
print(k_set)

# thêm kiểu dữ liệu 
k_set.add('10') #hash
#xóa đi phần tử có trong set
k_set.remove(9)#xóa phần tử có trong đó
#xóa phần tử ko có trong set mà ko bị lỗi nếu ko tìm thấy
k_set.discard(1000)
#xóa ngẫu nhiên 1 phần tử 
k_set.pop()
#xóa toàn bộ
k_set.clear()


set1=set([1,5,3,6,5])
set2 = set([3,5,9,8,7,10])
# hợp set với nhau 
set1 | set2
set1 & set2 #giao 
set1 - set2 # những cái nào có ở set2 thì bỏ đi ở set1
set1 ^ set2 # các phần tử ko trùng nhau của 2 set 