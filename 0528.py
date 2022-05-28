# 2022년 5월 28일 백준 알고리즘 풀이
import sys

# 11654번
#>N = sys.stdin.readline().strip()[:1]
#>print(ord(N))




# 11720번
#>N = int(sys.stdin.readline())
#>A = sys.stdin.readline().strip()[:N]
#>answer_list = []
#>for i in str(A):
#>    answer_list.append(int(i))
#>print(sum(answer_list))





# 10809번
#>input_value = sys.stdin.readline().strip()
#>input_list =[]
#>answer_list = []
#>for i in str(input_value):
#>    input_list.append(ord(i))
#>for i in range(97,123):
#>    if i in input_list:
#>        answer_list.append(input_list.index(i))
#>    else:
#>        answer_list.append(-1)
#>print(' '.join(map(str,answer_list)))

#(배운 것) ' '.join(map(str,answer_list)) 공백으로 구분하여 리스트 출력
#(배운 것) 순서를 사용해야 하면 집합 대신 리스트를 사용한다.
#(배운 것) 알파벳 반복과 같이 문자열을 반복해야 한다면 아스키 코드를 사용해 반복해보자.





# 2675번
#>N = int(sys.stdin.readline())
#>input_list = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
#>for i in range(len(input_list)):
#>    answer_list = []
#>    A = int(input_list[i][0])
#>    for l in str(input_list[i][1]):
#>        answer_list.append(l*A)
#>    print(''.join(map(str,answer_list)))







# 1157번
input_value = sys.stdin.readline().strip().upper()
input_list = []
answer_list = []
for i in str(input_value):
    input_list.append(i)
for i in input_list:
    answer_list.append(input_list.count(i))
answer_set = set()
for i in range(len(answer_list)):
    if answer_list[i] == max(answer_list):
        answer_set.add(input_list[i])
if len(answer_set) > 1:
    print("?")
else:
    print(list(answer_set)[0])