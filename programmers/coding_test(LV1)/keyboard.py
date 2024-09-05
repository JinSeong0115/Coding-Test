def solution(keymap, targets):
    keyboard = {}
    result = []
    
    for k in keymap:
        for i, a in enumerate(k):
            if a not in keyboard:
                keyboard[a] = i+1
            else:
                keyboard[a] = min(i+1, keyboard[a])
    
    for t in targets:
        times = 0
        for a in t:
            if a not in keyboard:
                times = -1
                break
            else:
                times += keyboard[a]
        result.append(times)
    
    return result