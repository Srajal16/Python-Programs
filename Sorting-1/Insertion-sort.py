'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key =  arr[i]
        j = i-1
        while(j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = key
   
    




arr = [21,45,64,87]
insertionSort(arr)
print(arr)