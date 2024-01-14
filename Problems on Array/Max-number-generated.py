'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def findMaxNum(array,n):
    array.sort(reverse = True)
    
    num = arr[0]
    
    for i in range(1,n):
        num = num*10 + arr[i]
    
    return num
    
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 0]
    n = len(arr)
    print(findMaxNum(arr, n))
    
    
