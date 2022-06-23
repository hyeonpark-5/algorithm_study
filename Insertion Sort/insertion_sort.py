temp = 0
j = 0

array =[1,10,5,8,7,6,4,3,2,9]
for i in range(0,10):
    j = i
    print("j = %d"%j)
    print("array= %d\n"%array[j])
    while array[j] > array[j+1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        j-=1
   

   




print(array)