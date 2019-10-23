a=[[1,2,3,4],
   [5,6,7,8],
   [9,1,2,3]]
b=[[1,2,3,4],
   [5,6,7,8],
   [9,1,2,3]]
matrix=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            matrix[i][j]+=a[i][k]*b[k][j]
for p in matrix:
    print(p)
