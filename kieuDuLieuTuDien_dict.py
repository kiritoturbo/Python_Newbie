#dict đều có cặp key : value
tu_dien ={
    'ten':'truong',
    'tuoi':26,
    'nghe':'lập trình',
    'bo_phan':['chan', 'tay']
}

print(tu_dien['ten'])
tu_dien['nghe']='MMO'
print(tu_dien['nghe'])
# xóa trong từ điển
del tu_dien['bo_phan']
print(tu_dien)
# trích tất cả các key 
L =[]
for i in tu_dien.keys():
    L.append(i)
print(L)
# trích tất cả các value 
L =[]
for i in tu_dien.values():
    L.append(i)
print(L)
# trích tất cả các keys,value 
L =[]
L1 =[]
for key,value in tu_dien.items():
    L.append(key) 
    L1.append(value) 
print(L)