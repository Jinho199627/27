# 2022년 5월 29일 백준 알고리즘 풀이
import sys

# 1152번
#a = 1
##>.strip()
#value = ' '.join(input_value.split()).strip()
#for i in str(value):
#    if i == " ":
#        a = a + 1
#print(a)

# 위 처럼 푸는 게 아니라
#>input_list = sys.stdin.readline().split()
#>print(len(input_list))
#(배운 것) 단어라면 단어의 성질에 초점을 맞춰서 푼다.







# 2908번
#>def reverse(a):
#>    answer = ''
#>    for i in str(a):
#>        answer = i + answer
#>        #(배운 것) 간단한 트릭으로 문자열을 뒤짚을 수 있다.
#>    return answer

#>A, B = map(int, sys.stdin.readline().split())
#>if int(reverse(A)) < int(reverse(B)):
#>    print(reverse(B))
#>else:
#>    print(reverse(A))






# 5622번
def to_num_sec(W):
    if W == 'Z':
        W = int(ord(W))-2
    elif int(ord(W)) >= 83:
        W = int(ord(W))-1
    else:
        W = int(ord(W))
    W = (W - 59) // 3
    return W + 1

#>input_value = sys.stdin.readline().strip()
#>answer = 0
#>for i in str(input_value):
#>    answer = answer + to_num_sec(i)
#>print(answer)





# 2941번
#>croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
#>input_value = sys.stdin.readline().strip()
#>for i in croatia:
#>    input_value = input_value.replace(i,'A')
#>print(len(input_value))






# 1316번
def group_word(input_value):
    for i in str(input_value):
        while i*2 in input_value:
            input_value = input_value.replace(i*2,i)
    #(배운 것) 특정 문자가 여러 번 나오면 i*2로 체크해주고 i*2를 i로 바꿔서 여러 번 나온 걸 한 번으로 고칠 수 있다.
    if len(input_value) == len(set(input_value)):
        b = 1
    else:
        b = 0
    return b

N = int(sys.stdin.readline())
input_list = [sys.stdin.readline().strip() for _ in range(N)]
answer = 0
for l in input_list:
    answer = answer + group_word(l)
print(answer)