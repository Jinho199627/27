# 2022년 05월 26일 백준 알고리즘 풀이
from re import A
import sys

# 3052번
#>input_list = [int(sys.stdin.readline()) for _ in range(10)]
#>answer_set = set()
#(배운 것) 빈 집합을 생성할 땐 set()을 해준다.

#>for i in input_list:
#>    answer_set.add(i % 42)
#(배운 것) set에서 원소를 추가할 땐 append가 아닌 add해준다.
#>print(len(answer_set))
#(배운 것) set 길이를 구하는 방법은 리스트와 똑같이 len을 해주는 것이다.






# 1546번
#>N = int(sys.stdin.readline())
#>input_list = list(map(float, sys.stdin.readline().split()))[:N]
#>answer_list = []

#>for i in input_list:
#>    answer_list.append(i/max(input_list)*100)

#>print(sum(answer_list)/len(answer_list))
#(배운 것) 리스트 값들의 평균을 구하는 함수는 따로 없고 sum함수와 len함수를 사용한다.







# 8958번
#>N = int(sys.stdin.readline())
#>input_list = [list(str(sys.stdin.readline()).strip()) for _ in range(N)]

#>for i in range(len(input_list)):
#>    a = 0
#>    b = 0
#>    for l in range(len(input_list[i])):
#>        if input_list[i][l] == "O":
#>            a = a + 1
#>            b = b + a
#>        else:
#>            a = 0
#>    print(b)
#(배운 것) 중간 연산이 필요한 게 있으면 반복문 안에 임의의 변수(a)를 설정해 중간 연산을 완료하고 최종 결과(b)에 반영한다.









# 4344번
N = int(sys.stdin.readline())
input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer_list = []

for i in range(N):
    A = 0
    answer_list = input_list[i][1:input_list[i][0]+1]
    average = sum(answer_list) / len(answer_list)
    for l in range(len(answer_list)):
        if average < answer_list[l]:
            A = A + 1
    print("{:.3f}%".format(round((A / len(answer_list))*100,3)))

