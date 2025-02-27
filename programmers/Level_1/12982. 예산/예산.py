def solution(d, budget):
    d = sorted(d)
    result = 0
    
    for i in range(len(d)):
        if sum(d[:i+1]) > budget:
            return result
        else:
            result += 1
    return result