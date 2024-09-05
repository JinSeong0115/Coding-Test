def solution(a, b, c, d):
    origin = list([a,b,c,d])
    set_origin = list(set(list([a,b,c,d])))
    
    if len(set_origin) == 1:  # 네 주사위에서 나온 숫자가 모두 같음
        return 1111*set_origin[0]
    elif len(set_origin) == 2:
        if origin.count(set_origin[0]) == 3:  # 세 주사위 같고 하나 다름 (index=0이 p)
            return (10*set_origin[0] + set_origin[1])**2
        elif origin.count(set_origin[0]) == 1:  # 세 주사위 같고 하나 다름 (index=0이 q)
            return (10*set_origin[1] + set_origin[0])**2
        else:
            return (set_origin[0]+set_origin[1])*abs(set_origin[0]-set_origin[1])
    elif len(set_origin) == 3:   # 3개 나올 때
        if origin.count(set_origin[0]) == 2:  # index=0이 p
            return set_origin[1]*set_origin[2]
        elif origin.count(set_origin[1]) == 2:  # index=1이 p
            return set_origin[0]*set_origin[2]
        else:  # index=2이 p
            return set_origin[0]*set_origin[1]
    else:  # 네 주사위가 모두 다름
        return min(origin)