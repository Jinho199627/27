# 2022년 5월 30일 백준 알고리즘 풀이
import sys
import math

# 1712번 (오류 코드 Zero Divison Error)
#>A, B, C = map(int, sys.stdin.readline().split())
#>if A/(C-B) <= 0:
#>    print(-1)
#>else:
#>    print(math.floor(A/(C-B))+1)

# 1712번 (오류 코드 해결)
#>A, B, C = map(int, sys.stdin.readline().split())
#>if (C-B) <= 0:
#>    print(-1)
#>else:
#>    print(math.floor(A/(C-B))+1)






# 2292번
#>N = int(sys.stdin.readline())
#>d = 1
#>i = 1
#>while d < N:
#>    d = d + (6 * i)
#>    i = i + 1
#>print(i)



# 1193번(풀긴 풀었는데 코드 정리 필요)
N = int(sys.stdin.readline())
d = 1
i = 2
while d < N:
    d = d + i
    i = i + 1
if (i - 1) % 2 == 1:
    k = d - i + 2
else:
    k = d
print("{0}/{1}".format(i-1-abs(k-N), 1+abs(k-N)))
