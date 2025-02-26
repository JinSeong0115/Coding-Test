def solution(str):
    str = str.split(" ")
    result = ""
    
    for s in str:
        for i, v in enumerate(list(s)):
            if i%2 == 0:
                result += v.upper()
            else:
                result += v.lower()
        result += " "
    
    return result[:-1]