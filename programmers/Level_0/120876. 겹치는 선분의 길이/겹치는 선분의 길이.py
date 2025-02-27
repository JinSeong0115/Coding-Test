def solution(lines):
    result = set()
    for i, a in enumerate(lines):
        for b in lines[i+1:]:
                result = result | set(set(range(a[0], a[1])) & set(range(b[0], b[1])))
    return len(result)

            