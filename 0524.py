# 22년 5월 24일 백준 알고리즘 풀이

import sys

# 11021번

#>Test_num = int(sys.stdin.readline())
#>input_list = []
#>input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(Test_num)]

#>for i in range(Test_num):
#>    print('Case #{0}: {1}'.format(i+1,sum(input_list[i])))






# 11022번
#>Test_num = int(sys.stdin.readline())
#>input_list = []
#>input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(Test_num)]

#>for i in range(Test_num):
#>    print('Case #{0}: {1} + {2} = {3}'.format(i+1, input_list[i][0], input_list[i][1], sum(input_list[i])))





# 2438번
#>Test_num = int(sys.stdin.readline())

#>for i in range(Test_num):
#>    print(' '*(Test_num-(1+i))+'*'*(1+i))

# (배운 것) 문자열을 연결해줄 땐 + 기호를 사용한다.



# 10871번
#>N, X = map(int,sys.stdin.readline().split( ))
#>input_list = list(map(int, sys.stdin.readline().split()))[:N]
# (배운 것) N개만 받으려면 입력 리스트를 N개만 남기고 슬라이싱 해주면 된다.

#>answer_list = []

#>for i in range(N):
#>    if X > input_list[i]:
#>        answer_list.append(input_list[i])

#>print(' '.join(str(i) for i in answer_list))
# (배운 것) 리스트 사이마다 무언갈 넣고 출력하려면 print 구문 안에 join을 활용한다.
# (배운 것) 숫자는 문자로 변환해서 조인 해줘야 한다.







# 10952번
# (배운 것) 특정 조건이 나올 때까지 입력을 받아야 한다면
A, B = map(int, sys.stdin.readline().split())
# (배운 것) 먼저 첫 번째 값을 입력 받고

sum_list = []
while A != 0 and B != 0:
# (배운 것) 그 값이 종료 조건에 해당하지 않으면
    sum_list.append(A+B)
    A, B = map(int, sys.stdin.readline().split())
# (배운 것) 하나를 더 받는다. 그리고 이걸 While로 반복

for i in range(len(sum_list)):
    print(sum_list[i])