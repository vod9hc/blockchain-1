board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Print Sodoku interface
def printSodoku(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
# Step 1: Find empty
def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j) #return row, col
    return None

# Check value inserted into pretty straightforward
def valid(bo, num, pos):
    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #Check col
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False 
    return True

# Use backtract algorithm
def solve(bo):
    find = findEmpty(bo)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(bo, i , (row, col)):
            bo[row][col] = i

            # thuật toán đệ quy. Nếu giá trị nhập vào hợp lệ theo điều kiện đã check thì sẽ trả về 1 mảng giá trị mới.
            if solve(bo):
                return True
            
            #Nếu không thoả sẽ đặt lại giá trị của cột đó = 0 quay lại thử tiếp giá trị tiếp tje==heo.
            bo[row][col] = 0
    return False
        
def main():
    printSodoku(board)
    solve(board)
    print("--------------------\n")
    printSodoku(board)

if __name__ == '__main__':
    main()