'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


  #Initialize matrix a  
a = [     
        [1, 2, 3],  
        [8, 6, 4],  
        [4, 5, 6]  
    ];  
   
#Calculates number of rows and columns present in given matrix  
rows = len(a);  
cols = len(a[0]);  
   
if(rows != cols):  
    print("Matrix should be a square matrix");  
else:  
    #Performs required operation to convert given matrix into lower triangular matrix  
    print("Lower triangular matrix: ");  
    for i in range(0, rows):  
        for j in range(0, cols):  
            if(j > i):  
                print("0",end = " "),  
            else:  
                print(a[i][j],end = " "),  
      
        print(" ");              
  