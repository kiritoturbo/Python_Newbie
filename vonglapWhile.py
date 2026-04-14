# <câu lệnh> 
# while < điều kiện> : 
#     <câu lệnh>

# yêu cầu người dùng nhập vào  số dương, nếu nhập sai thì bắt nhập lại 
a = float(input('nhập vào a dương = '))
while a<=0: 
    a=float(input('nhập lại a='))
print(f'nhập đúng a={a}')

#break : thoát khỏi vòng lặp
# in liên tiếp các số từ 1 đến 40 , nếu gặp số chia hết cho 30 thì lập tức dừng lại và in 'kết thúc" '
for i in range(1,41):
    if(i%30==0):
        print(f"kết thúc tại i = {i}")
        break
    else:
        print(i)


#continue : bỏ qua lần lặp 
# in liên tiếp các só từ 1 đến 70 , nếu gặp số chia hết cho 30 thì bỏ qua và in các số tiếp theo 
for i in range(1,71):
    if(i%30==0):
        continue
    else:
        print(i)