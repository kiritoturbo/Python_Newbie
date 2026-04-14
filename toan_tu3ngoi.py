# < Giá trị nếu đúng > if <điều kiện> else <giá trị nếu sai>
# Nhập vào 1 số dương và xem có phải số chính phương không 

a = float(input('a='))
import math

if math.sqrt(a) - math.ceil(math.sqrt(a)) == 0 : 
    print('số chính phương')
else : 
    print(' không phải số chính phương')

# toán tử 3 ngôi 
print('số chính phương ') if math.sqrt(a) - math.ceil(math.sqrt(a)) == 0 else print('không phải số chính phương')