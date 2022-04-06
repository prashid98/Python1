#nested List Comprehension 
matrix1 = []
for i in range(10):
    matrix1.append([])
    for j in range(10):
        matrix1[i].append(j)
print(matrix1)
#using nested list comprehension above example can be given as:
matrix2= [[j for j in range(10) ] for i in range(10)]
print(matrix2)

matrix3= [j for i in matrix2 for j in matrix1]
print(matrix3)
