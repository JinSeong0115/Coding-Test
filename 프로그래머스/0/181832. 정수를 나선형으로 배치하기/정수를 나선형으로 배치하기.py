def solution(n):
    result = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0  # x,y 좌표
    dir = 'r'
    i = 1
    
    while i <= n*n:
        if dir == 'r':  # 오른쪽으로 가는 경우
            result[y][x] = i
            if x == n-1 or result[y][x+1] != 0:  # 방향 바꾸는 조건
                dir = 'd'
                y += 1
            else:
                x += 1
            i += 1
            continue
        if dir == 'd':  # 아래쪽으로 가는 경우
            result[y][x] = i
            if y == n-1 or result[y+1][x] != 0:  # 방향 바꾸는 조건
                dir = 'l'
                x -= 1
            else:
                y += 1
            i += 1
            continue
        if dir == 'l':  # 왼쪽으로 가는 경우
            result[y][x] = i
            if x == 0 or result[y][x-1] != 0:  # 방향 바꾸는 조건
                dir = 'u'
                y -= 1
            else:
                x -= 1
            i += 1
            continue
        if dir == 'u':  # 위쪽으로 가는 경우
            result[y][x] = i
            if y == 0 or result[y-1][x] != 0:  # 방향 바꾸는 조건
                dir = 'r'
                x += 1
            else:
                y -= 1
            i += 1
            continue
    
    return result