# 2022년 06월 02일
import sys
# (내가 한번 만들어본 코드)
def not_prime(k):
    not_prime_number = set({1})
    for i in range(2,k+1):
        l = 2
        while (i * l) <= k:
            not_prime_number.add(i * l)
            l = l + 1
    return not_prime_number

# (아래는 에라토스테네스의 채 모형)
def Erato(k):
    a = [False, False] + [True]*(k-1)
    prime = []

    for l in range(2, k+1):
        if a[l]: #(배운 것) bool 리스트를 만들고 bool 리스트의 값을 슬라이싱한 결과를 if문에 사용할 수 있다.
            #(배운 것) 만약 해당 위치의 요소 값이 True였을 경우 실행되는 코드
            prime.append(l)
            for j in range(2*l, k+1, l):
                a[j] = False #(배운 것) 특정 요소들을 False로 바꿔줘서 위 if문과 연동할 수 있다.
    return prime

# 1978번

#>N = int(sys.stdin.readline())
#>input_list = list(map(int, sys.stdin.readline().split()))[:N]
#>answer_set = set()
#>for i in input_list:
#>    if i not in not_prime(max(input_list)):
#>        answer_set.add(i)
#>print(len(answer_set))





# 2581번
#>M = int(sys.stdin.readline())
#>N = int(sys.stdin.readline())
#>answer_set = set()
#>index_not_prime = not_prime(N)
#(배운 것) 특정 수열 중 소수인 것들을 찾을 땐 가장 큰 수만큼 소수의 행렬을 생성해놓고 특정 수열과 비교한다.

#>for i in range(M,N+1):
#>    if i not in index_not_prime:
#>        answer_set.add(i)
#>if len(answer_set)>0:
#>    print(sum(answer_set))
#>    print(min(answer_set))
#>else: print(-1)







# 시간비교(내가 짠 코드보다 비교용으로 가져온 에라토스테네스의 채가 20배 이상 빠르다.)
#>import time
#>start = time.time()

#print(Erato(1000000))

#>print("time :", time.time() - start)

#>start = time.time()

#>not_prime(1000000)

#>print("time :", time.time() - start)




# 11653번(에라토스테네스 채를 이용해 소수를 생성하고
# 그걸 하나씩 반복문 돌리며 소인수 분해를 해서 풀 수도 있다.
# 그러나 이렇게 풀면 비효율적이다.
# 왜냐하면 후반부의 소수가 사용 안 될 수 있는데 굳이 구하는 것이기 때문.)
N = int(sys.stdin.readline())
for i in range(2,N+1):
    while N != 1:
        while divmod(N,i)[1] == 0:
            print(i)
            N = (N/i)
        break