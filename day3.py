import re

def mul(x,y):
    return x * y

with open("input.txt", 'r') as file:
    file_content = file.read()

# print(file_content)

ans = 0
lines = file_content
disable = False
for i in range(len(lines)):
    if lines[i:i+3] == "do(":
        j=i+3
        if lines[j]==")":
            disable = False

    if lines[i:i+6] == "don't(":
        j=i+6
        if lines[j]==")":
            disable = True

    if lines[i:i+4] == "mul(":
        j = i+4
        while lines[j]!=")":
            j += 1
        try:
            x,y = map(int, re.findall('\d+',lines[i:j+1]))
            if lines[j-1] not in ['0','1','2','3','4','5','6','7','8','9']:
                continue

            if not disable:
                ans += x * y
            # print(ans)
            # print(lines[i:j+1])
        except:
            pass


print(ans)
