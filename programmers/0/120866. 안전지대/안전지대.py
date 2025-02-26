def solution(board):
    n = len(board)  # 길이
    
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            
            if value == 1:
            
                for xx in [-1,0,1]:
                    for yy in [-1,0,1]:
                    
                        if 0<=x+xx<n and 0<=y+yy<n and board[x+xx][y+yy]!=1:
                            board[x+xx][y+yy] = 'x'
    return sum([i.count(0) for i in board])
                
                
        