import sys
from collections import defaultdict, Counter
# infile = sys.argv[1] if len(sys.argv) >= 2 else
# D = open(infile).read().split()
lines = []

while True:
    try:
        acc = input().split()
        for i in range(len(acc)):
            acc[i] = int(acc[i])
        lines.append(acc)
    except EOFError:
        break

ans = 0
for line in lines:
    print("Hi")
    xs1 = line
    # print(xs1)
    good = False
    for j in range(len(xs1)):
        xs = xs1[:j] + xs1[j+1:]
        inc_or_dec = (xs==sorted(xs) or xs==sorted(xs,reverse=True))
        ok = True
        for i in range(len(xs)-1):
            diff = abs(xs[i]-xs[i+1])
            if not 1<=diff<=3:
                ok = False
        if inc_or_dec and ok:
            good = True
    if good:
        ans += 1

print(ans)