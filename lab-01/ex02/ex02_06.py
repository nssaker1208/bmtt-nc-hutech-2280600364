#Nhập 2 số X và Y xây dựng mảng 2 chiều 
input_str = input("Nhập X, Y: ")
dimentions = [int(x) for x in input_str.split(',')]
so_dong = dimentions[0]
so_cot = dimentions[1]
multilist = [[0 for j in range(so_cot)] for i in range(so_dong)]
for i in range(so_dong):
    for j in range(so_cot):
        multilist[i][j] = i*j
print(multilist)