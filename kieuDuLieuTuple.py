# tuple là một kiểu dữ liệu có cấu trúc dùng để lưu trữ nhiều giá trị trong một biến duy nhất.Tuple rất giống với list, nhưng có đặc điểm nổi bật là không thể thay đổi sau khi được tạo ra 
tp = (1,2,3)
# hoặc khởi tạo như này tp=1,2,3. Để tp =(1,) phải bắt buộc có dấu phẩy mới là tuple
print(tp[1])
print(type(tp)) # kiểm tra kiểu dữ liệu
tp = ('h','e','l','l','o','w','o','r','l','d')
dem = 0
for i in tp:
    if i == 'l':
        dem +=1 #dem = dem + 1
print('ký tự ''l'' lặp lại ', dem, 'lần')

# cách khác 
print(tp.count('l')) #đếm số lần lặp lại của ký tự "l"
print(tp.index('l')) #đếm chỉ số xuất hiện ký tự "l"