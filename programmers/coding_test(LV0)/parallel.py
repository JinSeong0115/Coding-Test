def solution(dots):
    ar = []
    for i in range(3):
        for j in range(i+1, 4):
            v1, v2 = dots[i], dots[j]
            ar.append((v1[1]-v2[1]) / (v1[0]-v2[0]))
    for k in range(3):
        if ar[k] == ar[5-k]:
            return 1
        else:
            return 0