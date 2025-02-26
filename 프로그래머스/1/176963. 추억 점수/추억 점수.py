def solution(name, yearning, photo):
    result = []
    
    score = {n:y for n,y in zip(name, yearning)}
    
    result = [sum(score.get(pl, 0) for pl in p) for p in photo]
    return result
            
    