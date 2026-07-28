# 1. Define the 2D matrix (a list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Loop through each row
for row in matrix:
    # 3. Join the numbers together without spaces
    for num in row:
        print(num, end="")
    print() # Moves to the next line after finishing a row
