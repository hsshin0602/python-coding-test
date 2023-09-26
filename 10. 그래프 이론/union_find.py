# 재귀적으로 부모 찾기
def find_parent(parent, x):
    # 루트노드 찾기, 부모테이블의 값과 본인 값이 다르면 루트가 아님
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 경로 압축기법: 최종 루트로 부모테이블 갱신
def find_parent_root(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    # a,b의 부모찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 작은 값이 루트값
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 자기자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 부모 갱신
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")
print()
print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")
