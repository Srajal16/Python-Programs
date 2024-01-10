'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def reverArray(A, start, end):
    if start>= end:
        return
    A[start], A[end] = A[end], A[start]
    reverArray(A,start+1,end-1)
    
A = [10, 20, 30, 40, 50]
reverArray(A, 0, 4)
print(A)
