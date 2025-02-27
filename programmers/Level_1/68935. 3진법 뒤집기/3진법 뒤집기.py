def solution(n):
    if n <= 2:
        return n
    
    three = ""
    result = 0
    
    while n > 8:
        three += str(n%3)
        n = n//3
    
    three += str(n%3)
    three += str(n//3)
    
    for i, v in enumerate(reversed(three)):
        result += int(v)*(3**int(i))
    
    return result
