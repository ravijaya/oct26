mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mat[1].insert(2, 'y')
# mat[1][1] = 'x'  # update an item
print(mat)
print()
exit(1)

del mat[0][1]  # delete an item
mat[2].append(10) # append an item to the row
print(mat)
print()

mat.insert(2, [11, 22, 33])   # insert a row
print(mat)
print()

for row in mat:
    for col in row:
        print(col, end='\t')
    print()
