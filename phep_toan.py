'''
Nhập vào 2 số nguyên a và b rồi in ra màn hình : 
tổng , hiệu ,tích, thương (dư, nguyên , thập phân)
căn bậc 2 , trị tuyệt đối , mũ 2 , mũ 3 (cell)
'''
import math

a = int(input('Nhập a = '))
b = int(input('Nhập b = '))
tong= a + b
hieu = a - b
tich = a * b
thuong_du = a % b  # chia lấy dư của a cho b
thuong_nguyen = a // b # chia lấy nguyên
thuong_thap_phan = a / b # chia lấy thập phân
print('Tổng = ',tong)
print(f'Hiệu = {hieu}')
print(f'Tích = {tich} \n')
print(f'Thương dư = {thuong_du} \n')
print(f'Thương Nguyên = {thuong_nguyen} \n')
print(f'Thương thập phân = {thuong_thap_phan} \n')

can_bac_hai = math.sqrt(a) # căn bậc 2 
lam_tron_ham_thap_phan = round(can_bac_hai)# làm tròn dựa vào phần thập phân
lam_tron_xuong = math.floor(can_bac_hai) #làm tròn xuống
lam_trong_len = math.ceil(can_bac_hai) # làm tròn lên
print(f'Căn bậc hai của a là {can_bac_hai}')