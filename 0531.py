# 2022년 5월 31일 백준 알고리즘 풀이
from re import L
import sys
import math

# 2869번
#>A, B, V = map(int, sys.stdin.readline().split())
# A: 낮에 올라가는 길이
# B: 밤에 내려가는 길이
# V: 나무의 길이
#>print(math.ceil((V-A)/(A-B))+1)
#(배운 것): 바로 풀이로 들어가지 말고 최대한 계산을 줄일 수 있는 방법을 생각해보자





# 10250번
def room_number(A, B, C):
    if divmod(C-1,A)[0]+1 < 10:
        print("{0}0{1}".format(divmod(C-1,A)[1]+1,divmod(C-1,A)[0]+1))
    else:
        print("{0}{1}".format(divmod(C-1,A)[1]+1,divmod(C-1,A)[0]+1))

#>N = int(sys.stdin.readline())
#>input_list = [list(map(int, sys.stdin.readline().split()))[:3] for _ in range(N)]
#>for i in range(N):
#>    room_number(input_list[i][0], input_list[i][1], input_list[i][2])
#(배운 것) 1~6은 1이 나와야 하고, 7~12는 2가 나와야 한다.
#(배운 것) 이때 6으로 나눠서 몫을 구하려고 하면 마지막 숫자인 6과 12가 규칙에 부합하지 않는데
#(배운 것) 이럴 땐 전체적으로 -1을 해주는 등 간단히 방향을 틀어주면 쉽게 해결된다.






# 2775번(푸는 중)
# 2022년 6월 1일 풀이완료
def apartment(K, N):
    apartment_list = []
    add_list = []
    for i in range(N):
        add_list.append(i+1)
    apartment_list.append(add_list)
    for i in range(1, K+1):
        add_list = []
        add_list.append(1)
        for l in range(1,N):
            add_list.append(add_list[l-1]+apartment_list[i-1][l])
        apartment_list.append(add_list)
    return apartment_list[K][N-1]        
#(배운 것) 수열을 만들 때 계속 전 단계를 참고해야 한다면 한번 전체 전개도를 만드는 것도 방법이다.

#>T = int(sys.stdin.readline())
#>input_list = [int(sys.stdin.readline()) for _ in range(T*2)]
#>for m in range(T):
#>    print(apartment(input_list[m*2], input_list[m*2+1]))
