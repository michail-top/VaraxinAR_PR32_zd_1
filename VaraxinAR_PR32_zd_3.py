n = int(input())
male = list(map(int, input().split()))
m = int(input())
female = list(map(int, input().split()))

male.sort()
female.sort()

male.reverse()
female.reverse()

ans = 0
i = 0

if n > m:
    for fem in female:
        if fem <= male[i]:
            ans += 1
            
            i+=1
            if i >= n:
                break
else:
    for men in male:
        if men >= female[i]:
            ans += 1       
            i+=1
            if i >= n:
                break

print(ans)
