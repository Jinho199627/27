# 2022년 06월 03일 백준 알고리즘 풀이
import sys
import time
sys.setrecursionlimit(10**7)

def Erato(k):
    a = [False, False] + [True]*(k-1)
    prime = []

    for l in range(2, k+1):
        if a[l]:
            prime.append(l)
            for j in range(2*l, k+1, l):
                a[j] = False
    return prime


# 1929번
#>M, N = map(int, sys.stdin.readline().split())
#>prime_list = Erato(N)
#>for i in prime_list:
#>    if i >= M and i <= N:
#>        print(i)





# 4948번
#>N = int(sys.stdin.readline())
#>input_list = []
#>while N != 0:
#>    input_list.append(N)
#>    N = int(sys.stdin.readline())
#>prime_list = Erato(max(input_list)*2)
#>answer_set = set()
#>for i in input_list:
#>    for l in prime_list:
#>        if l > i and l <= 2*i:
#>            answer_set.add(l)
#>        elif l > 2*i : break #(배운 것) 불필요한 반복을 최대한 줄이기 위해 특정 조건이 되면 break 되게 하자.
#>    print(len(answer_set))
#>    answer_set.clear()





# 9020번(푸는 중. 골드바흐의 추측)
#>N = int(sys.stdin.readline())
#>input_list = [int(sys.stdin.readline()) for _ in range(N)]





# 10872번
# 일반적으로 for문 사용 코드
def factorial(a):
    b = 1
    while a >= 1:
        b = b*a
        a = a - 1
    return b
def fact(a):
    b = 1
    if a >= 0:
        b = a * fact(a-1)
    return b
#>start = time.time()
#>N = int(sys.stdin.readline()) #(배운 것) 1000을 넣었을 땐 재귀함수가 빨랐으나 재귀함수는 특정 반복이 넘어가면 에러가 나온다.
#>factorial(N)
#>print("time :", time.time() - start)
#>start = time.time()
#>fact(N)
#>print("time :", time.time() - start)





# 10870번
def Fibo(a):
    if a == 0:
        b = 0
    elif a == 1:
        b = 1
    else: b = Fibo(a-1) + Fibo(a-2)
    return b
print(Fibo(int(sys.stdin.readline())))
