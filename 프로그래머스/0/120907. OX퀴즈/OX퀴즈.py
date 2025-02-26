def solution(quiz):
    a = []
    result = []
    for i in quiz:
        a = i.replace(" ","").split("=")
        if eval(a[0]) == int(a[1]):
            result.append("O")
        else:
            result.append("X")
            
    return result