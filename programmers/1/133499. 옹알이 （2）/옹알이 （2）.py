def solution(babbling):
    pron = ["aya", "ye", "woo", "ma"]
    result = 0
    
    for b in babbling:
        for p in pron:
            if p*2 in b:
                break
            b = b.replace(p, "1")
            if set(list(b)) == set("1"):
                result += 1
                break
                
    return result