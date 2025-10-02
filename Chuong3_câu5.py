#Hãy cho biết kết quả xuất ra màn hình

#i,j,k = 3,5,7
#Kết quả: i =  5  j =  5  k =  7

#i,j,k = 3,7,5
#Kết quả: i =  3  j =  5  k =  5

#i,j,k = 5,3,7
#Kết quả: i =  5  j =  7  k =  7

#i,j,k = 5,7,3
#Kết Quả: i =  5  j =  3  k =  3

#i,j,k = 7,3,5
#Kết Quả: i =  7  j =  5  k =  5

i,j,k = 7,5,3
#Kết Quả: i =  7  j =  7  k =  3

if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        j=k
print("i = ",i," j = ",j," k = ",k)