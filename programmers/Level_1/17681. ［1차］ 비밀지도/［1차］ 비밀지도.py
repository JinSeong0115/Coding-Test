def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        value = bin(arr1[i] | arr2[i])[2:].zfill(n)
        value = str(value).replace("0", " ")
        value = value.replace("1", "#")
        answer.append(value)
    
    return answer