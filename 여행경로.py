from collections import *

tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
]
dict = defaultdict(list)
for st in tickets:
    dict[st[0]].append(st[1])

for i in dict:
    dict[i].sort(reverse=True)
print(dict)

stack = ["ICN"]
answer = []

while stack:
    top = stack[-1]
    if not dict[top]:
        answer.append(stack.pop())
    else:
        stack.append(dict[top].pop())
    print(stack)

print(answer[::-1])
