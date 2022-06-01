# 2022년 6월 1일 백준 알고리즘 풀이
import sys

# 2839번
#>N = int(sys.stdin.readline())
#>answer = -1
#>for i in range(0, 5):
#>    if divmod(N-(3*i),5)[1] == 0 and (N-(3*i)) >= 0:
#>        answer = divmod(N-(3*i),5)[0]+i
#>        break
    #(배운 것)N을 5로 나눈 나머지가 0, 3, 6, 9, 12라면 5와 3을 더해 수를 만들 수 있다.
#>if answer != 0:
#>    print(answer)
#>else:
#>    print(answer)

    




# 10757번
A, B = map(int, sys.stdin.readline().split())
print(A+B)