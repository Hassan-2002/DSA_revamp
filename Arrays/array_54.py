# Given an m x n matrix, return all elements of the matrix in spiral order.
def spiralOrder(matrix : list[list[int]]) -> list[int]:
    spiral = []
    top= left =0
    bottom = len(matrix) -1
    right = len(matrix[0])-1
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            spiral.append(matrix[top][i])
        top+=1 
        for i in range(top,bottom+1):
            spiral.append(matrix[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                spiral.append(matrix[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                spiral.append(matrix[i][left])
            left+=1
    return spiral
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = spiralOrder(matrix)
print(result)           
        