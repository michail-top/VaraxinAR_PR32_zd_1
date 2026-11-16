import math

n, k1, t1, k2, t2 = map(int, input().split())

petya = math.ceil(n / k1) * t1
brother = math.ceil(n / k2) * t2

print(min(petya, brother))
