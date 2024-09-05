def solution(board, h, w):
    oh, ow = len(board), len(board[0])
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    result = 0
    
    for i in range(4):
        if (0<=h+dh[i] and h+dh[i]<=oh-1) and (0<=w+dw[i] and w+dw[i]<=ow-1):
            if board[h][w] == board[h+dh[i]][w+dw[i]]:
                result += 1
    
    return result