def holes(board):
    board = [['0','1','0','1','0','1','0','1'],['1','0','1','0','1','0','1','0'],
             ['0','1','0','1','0','1','0','1'],['1','0','1','0','1','0','1','0'],
             ['0','1','0','1','0','1','0','1'],['1','0','1','0','1','0','1','0'],
             ['0','1','0','1','0','1','0','1'],['1','0','1','0','1','0','1','0'],]
    count = 0
    for i in range(8):
        for j in range(8):
            if (board[i][j] == '0' and dudu[i][j]=='F'):
                count += 1

    return count

# 입력 받기
dudu = [input().strip() for _ in range(8)]

# 두더지가 올라올 수 있는 칸의 개수 출력
result = holes(dudu)
print(result)
