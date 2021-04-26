a, b = map(int, input().strip().split(' '))
ans = ''
for i in range (0,b):
    for j in range (0,a):
        ans += '*'
    ans += '\n'
print(ans)