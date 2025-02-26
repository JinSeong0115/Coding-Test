def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        for p in pron:
            if p in babbling[i]:
                babbling[i] = babbling[i].replace(p, " ")
        if not len(babbling[i].strip()):
            answer += 1
    
    return answer