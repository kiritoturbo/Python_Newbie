# nhập vào 1 số nguyên và kiểm tra số đó là số chẵn hay lẻ 
a = int(input('nhập a='))
if a % 2 ==0 and a != 0:
        print('số chẵn')
elif a %2 !=0: 
    print('số lẻ')
else : 
    print('số 0')