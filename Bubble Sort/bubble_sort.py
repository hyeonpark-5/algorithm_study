temp = 0
array =[1,10,5,8,7,6,4,3,2,9 ]

for i in range(0,10):
    for j in range(0,9-i):                                                       
        if array[j] > array[j+1]:
            temp = array[j]
            array[j]=array[j+1]
            array[j+1] = temp

            

print(array)