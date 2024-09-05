def solution(n, lost, reserve):
    lost, reserve = set(lost) - (set(lost)&set(reserve)), set(reserve) - (set(lost)&set(reserve))
    
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    return n-len(lost)