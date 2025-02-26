def solution(number, limit, power):
    result = 0
    for i in range(1, number+1):
        div_num = 0
        for d in range(1, int(i**(1/2))+1):
            if i%d == 0:
                div_num += 1
                if i/d != d:
                    div_num += 1
            if div_num > limit:
                div_num = power
                break
        result += div_num
    return result