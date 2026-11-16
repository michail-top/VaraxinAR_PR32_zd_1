a = input()
b = input()
c = input()

ans = str()

for i in range(len(a)):
    ans += max(a[i], b[i], c[i])

print(ans)