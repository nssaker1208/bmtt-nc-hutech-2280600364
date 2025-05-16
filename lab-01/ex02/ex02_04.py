#Tìm all số từ 2000 đến 3200 chia hết cho 7 và ko phải bội của 5 và các số tìm đc ngăn cách bởi dấu phẩy

j=[]
for i in range(2000, 3201):
    if(i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(",".join(j))