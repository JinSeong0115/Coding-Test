def solution(s, n):
    result = []
    
    for i in s:
        if ord(i) != 32:
            for _ in range(n):    
                if ord(i) == 90 :
                    i = "A"
                elif ord(i) == 122:
                    i = "a"
                else:
                    i = chr(ord(i)+1)
        result.append(i)
    
    return ''.join(result)