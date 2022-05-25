# 2022년 5월 25일 백준 알고리즘 풀이
import sys
# 10951번
#>while True:
#>    try:
#>        A, B = map(int, sys.stdin.readline().split())
        # (배운 것) 두 개 이상을 받을 땐 map
#>        print(A + B)
#>    except:
#>        break
# (배운 것) While Ture로 무한 루프를 만들고 break로 반복문을 깨고 나온다.
# (배운 것) try 구문에서 오류가 나면 except로 온다.






# 1110번
#>Test_num = int(sys.stdin.readline())

#>A = Test_num // 10
# (배운 것) divmod는 큰 숫자 연산에선 빠르지만 작은 숫자 연산에서는 느리다.
#>B = Test_num % 10
#>C = (B * 10) + ((A + B) % 10)
#>i = 1

#>while Test_num != C:
#>    i = i + 1
#>    A = C // 10
#>    B = C % 10
#>    C = (B * 10) + ((A + B) % 10)

#>print(i)







# 10818번
#>N = int(sys.stdin.readline())
#>input_list = list(map(int, sys.stdin.readline().split()))[:N]

#>print('{0} {1}'.format(min(input_list), max(input_list)))







# 2562번
#>input_list = [int(sys.stdin.readline()) for _ in range(9)]

# (오류) [list(map(int, sys.stdin.readline())) for _ in range(9)]
# (원인) 1열인 것에 굳이 map(int,를 사용할 필요가 없다.
# (해결) [int(sys.stdin.readline()) for _ in range(9)]
#>print(max(input_list))

#>i = 0
#>while max(input_list) != input_list[i]:
#>    i = i + 1

#>print(i+1)








# 2577번
input_list = [int(sys.stdin.readline()) for _ in range(3)]
#> A = input_list[0] * input_list[1] * input_list[2]
#>answer = []

#>for i in str(A):
#>    answer.append(int(i))

answer = [int(i) for i in str(input_list[0] * input_list[1] * input_list[2])]

for i in range(10):
    print(answer.count(i))
