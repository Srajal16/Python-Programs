'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    




arr = [21,45,64,87]
bubbleSort(arr)
print(arr)