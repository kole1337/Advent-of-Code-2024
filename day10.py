import re
import heapq
from collections import deque

with open("input.txt", 'r') as file:
    D = file.read().strip()

p1 = 0
p2 = 0

G = D.split('\n')
G = [[int(x) for x in row] for row in G]
R = len(G)
C = len(G[0])

def ways1(sr,sc):
    """How many different 0s can I reach going down from here?"""
    Q = deque([(sr,sc)])
    ans = 0
    SEEN = set()
    while Q:
        r,c = Q.popleft()
        if (r,c) in SEEN:
            continue
        SEEN.add((r,c))
        if G[r][c]==0:
            ans += 1
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc] == G[r][c]-1:
                Q.append((rr,cc))
    return ans

DP = {}
def ways(r,c):
    if G[r][c]==0:
        return 1
    if (r,c) in DP:
        return DP[(r,c)]
    ans = 0
    for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
        rr = r+dr
        cc = c+dc
        if 0<=rr<R and 0<=cc<C and G[rr][cc] == G[r][c]-1:
            ans += ways(rr,cc)
    DP[(r,c)] = ans
    return ans

for r in range(R):
    for c in range(C):
        if G[r][c]==9:
            p1 += ways1(r,c)
            p2 += ways(r,c)

print(p1)
print(p2)