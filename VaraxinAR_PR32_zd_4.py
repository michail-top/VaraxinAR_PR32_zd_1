def add_stack(stack_, a_list, index):
    stack_.append(index)

    if len(stack_) == 1:
        return

    end, end_1 = len(a_list)-1, len(a_list)-2
    while end_1>=0 and a_list[end_1] < a_list[end]:
        (end, end_1) = (end_1, end)

s, n = map(int, input().split())

a_list = []
b_list = []

summ_a = 0
summ_b = 0
for i in range(n):
    b, a = map(int, input().split())
    summ_b += b
    summ_a += a

    a_list.append(a)
    b_list.append(b)

stack_ = []

ans = 0
ans_list = []

if s > summ_b:
    ans = 0
elif s+summ_a < summ_b:
    ans = -1
else:
    for i in range(n):
        while s < b_list[i]:
            if len(stack_) == 0:
                ans = -1
                break

            
            ans += 1
            ans_list.append(stack_[0]+1)
            s += a_list[stack_[0]]
            del stack_[0]

        s -= b_list[i]
        add_stack(stack_, a_list, i)


print(ans)        
if ans > 0: 
    print(*ans_list)