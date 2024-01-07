'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

arr = [2, 5,8,3,7]

l = len(arr)
ans = []
count = 0
for i in arr:
    for j in range(l):
        if(arr[j]-i)<0:
            count = count + 1
    ans.append(count)
    count = 0
print(ans)