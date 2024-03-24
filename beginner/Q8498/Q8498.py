rows = 8
matrix = []

count = 0

for i in range(rows):
    row = []
    
    user_input = input()
    row = [char for char in user_input]

    matrix.append(row)


for i in range(0,len(matrix)):
    for j in range(0, rows):
        if(matrix[i][j] == 'F'):
            if(((i+j)%2) ==0):
                count += 1
    
print(count)