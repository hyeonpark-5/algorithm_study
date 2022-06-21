temp = 0  
index = 0
array =[1,10,5,8,7,6,4,3,2,9 ]
for i in range(0,10):
    j = i
    min = 9999
    
    for j in range(i,10):
        if min > array[j]:
            min = array[j]
            index = j

    print(min)
    temp = array[i]
    array[i] = array[index]
    array[index] = temp


print(array)