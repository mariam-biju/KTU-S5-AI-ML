import numpy as np
row1=int(input("Enter the number of rows in first matrix: "))
col1=int(input("Enter the number of columns in first matrix: "))
arr1=np.zeros((row1,col1),dtype=int)
row2=int(input("Enter the number of rows in second matrix: "))
col2=int(input("Enter the number of columns in second matrix: "))
arr2=np.zeros((row2,col2),dtype=int)
if col1!=row2:
    print("Matrices cannot be multiplied")
else:
    print("Enter elements for the first matrix: ")
    for i in range(row1):
        for j in range(col1):
            arr1[i][j]=int(input(f"Element {[i],[j]}: "))
    print("First matrix: ")
    print(arr1)
    print("Enter elements for the second matrix: ")
    for i in range(row2):
        for j in range(col2):
            arr2[i][j]=int(input(f"Element {[i],[j]}: "))
    print("Second matrix: ")
    print(arr2)
    print("Matrices Multiplied: ")
    arr3=np.dot(arr1,arr2)
    print(arr3)
    
