def solution(ingredient):
    result = 0
    stack = []
    burger = [1, 2, 3, 1]
    
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == burger: 
            result += 1
            del stack[-4:] 
    
    return result
