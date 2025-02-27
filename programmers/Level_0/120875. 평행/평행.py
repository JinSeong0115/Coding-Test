def solution(dots):
    def slope(p1, p2):
        if p1[0] == p2[0]:
            return float('inf')
        return (p1[1] - p2[1]) / (p1[0] - p2[0])

    pairs = [
        (dots[0], dots[1], dots[2], dots[3]),  # A-B, C-D
        (dots[0], dots[2], dots[1], dots[3]),  # A-C, B-D
        (dots[0], dots[3], dots[1], dots[2])   # A-D, B-C
    ]

    for p1, p2, p3, p4 in pairs:
        if slope(p1, p2) == slope(p3, p4):
            return 1
    return 0
