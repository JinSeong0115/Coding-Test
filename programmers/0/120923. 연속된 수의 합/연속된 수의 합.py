def solution(num, total):
    standard = total//num
    if num%2 == 0:
        return [standard+i for i in range(-(num//2-1),num//2+1)]
    return [standard+j for j in range(-(num//2), num//2+1)]