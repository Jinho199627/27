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







# 1157번(답은 맞게 나오는데 시간 초과됐다. 다시 풀어보자.)
# 22년 5월 29일에 풀이 완료.
input_value = sys.stdin.readline().strip().upper()
input_dict = dict()
answer_list = []
for i in str(input_value):
    if i not in input_dict:
        input_dict[i] = 1
    else:
        input_dict[i] = input_dict[i] + 1
#(배운 것) 딕셔너리 추가는 생각보다 간편하다. 그냥 키와 값을 선언해주면 된다.
#(배운 것) 딕셔너리는 not in 등으로 있는지 체크할 때 특별히 언급해주지 않으면 key값 기준으로 체크한다.
for i in input_dict:
    if input_dict[i] == max(input_dict.values()):
#(배운 것) 딕셔너리에서 값 기준으로 무언갈 하고 싶으면 .values()로 값을 사용할거라고 선언해준다.
        answer_list.append(i)
if len(answer_list) > 1:
    print("?")
else:
    print(answer_list[0])
