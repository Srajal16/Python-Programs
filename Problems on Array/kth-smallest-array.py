'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def kthsmallest(arr, N, k):
    arr.sort()
    
    return arr[k-1]
    
if __name__ == "__main__":
    
    arr = [12,3,5,7,19]
    N = len(arr)
    K = 2
    print("Kth smallest element is", kthsmallest(arr,N,K))
