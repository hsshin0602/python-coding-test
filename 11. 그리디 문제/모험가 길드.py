n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
member = []
for i in range(n):
    member.append(arr[i])
    if max(member) > len(member):
        continue
    else:  # 모험가 공포가 사람수보다 작거나 같음
        cnt += 1
        member.clear()
print(cnt)

"""
# 더 간편한 방법
count=0
 for data in arr:
    count+=1
    if count >= data:
        cnt+=1
        count=0
"""
