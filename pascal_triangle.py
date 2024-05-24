def print_pascal_triangle(height):
    for i in range(height):
        for _ in range(height-i-1):
            print(" ", end="")
        for j in range(i+1):
            print(pascal(i,j),end=" ")
        print()

def pascal(row,col):
    if col==0 or col==row:
        return 1
    else:
        return pascal(row-1, col-1)+pascal(row-1,col)

height =8
print_pascal_triangle(height)
