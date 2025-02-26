def gcd(a, b):
    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b%i == 0:
            return i

def solution(numer1, denom1, numer2, denom2):
    denom = denom1*denom2
    numer = numer1*denom2 + numer2*denom1
    g = gcd(denom,numer)
    return [numer//g, denom//g]