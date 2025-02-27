def gcd(n, m):
    for i in range(max(n,m), 0, -1):
        if n%i == 0 and m%i == 0:
            return i

def lcm(n, m):
    return n*m / gcd(n,m)
    


def solution(n, m):
    return [gcd(n, m), lcm(n, m)]