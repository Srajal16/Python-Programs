n=int(10)
k=int(input())
if(k==0):
    print("INVALID INPUT")
    print("NUMBER OF CANDIES AVAILABLE: ",n)
else:
    print("NUMBER OF CANDIES SOLD: ",k)
    print("NUMBER OF CANDIES AVAILABLE: ",n-k)