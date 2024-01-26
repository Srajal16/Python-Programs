'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = arr[0]
        for j in range(i+1,n):
            
            if(arr[i]>arr[j]):
                
                mini = arr[j]
                arr[i],arr[j] = arr[j],arr[i]
    




arr = [21,45,64,87,21]
selectionSort(arr)
print(arr)