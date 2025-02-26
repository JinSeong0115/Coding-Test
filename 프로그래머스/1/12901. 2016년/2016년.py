def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dates = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    if a > 1:
        return dates[(sum(days[:a-1])+b)%7]
    return dates[b%7]