def solution(a, b, n):
    answer = 0
    
    while n >= a:
        new_coke = (n//a)*b
        remain_coke = n%a
        
        answer += new_coke 
        n = new_coke + remain_coke
        
    return answer
        