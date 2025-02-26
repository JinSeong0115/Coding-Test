def solution(t, p):
    return len(["_" for i in range(0, len(t)+1-len(p)) if int(t[i:i+len(p)]) <= int(p)])
    
            