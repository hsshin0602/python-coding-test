N = int(input())
order = list(input().split())

located = [1, 1]

for check in order:
    if check == "L" and located[1] > 1:
        located[1] -= 1
    elif check == "R" and located[1] < N:
        located[1] += 1
    elif check == "U" and located[0] > 1:
        located[0] -= 1
    elif check == "D" and located[0] < N:
        located[0] += 1
print(located)
