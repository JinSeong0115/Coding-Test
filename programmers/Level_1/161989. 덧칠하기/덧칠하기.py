def solution(n, m, section):
    result = 1
    i = 0
    j = 0
    
    while i <= len(section)-1:
        if section[i] in range(section[j], section[j]+m):
            i += 1
        else:
            j = i
            result += 1
    
    return result