import math
try: 
    a = int(input('a='))
    kq=10/a
except ZeroDivisionError:
    print('lỗi ko chia cho 0')
except ValueError:
    print('nhập kí tự, nhập số đi')
else:
    print(math.ceil(kq))
finally:
    print("kết thúc")