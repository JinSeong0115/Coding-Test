def solution(s):
    answer = {}
    count = 0
    length = 0
    
    for i in s:
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1
        length += 1
        if length/2 in answer.values():
            count += 1
            length = 0
            answer = {}
    
    if length != 0:
        return count + 1
    return count