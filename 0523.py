# 22년 5월 23일 백준 알고리즘 풀이

# 10950번
#>range_size = int(input())
#>s_list = [list(map(int, input().split(" "))) for _ in range(range_size)]
# 열은 띄어쓰기로 행은 엔터로 구분하여 입력을 받는다. 2차원 배열 생성하기

#>for i in s_list:
#>    print(sum(i))





# 8393번
#>A = int(input())
#>B = 0

#>for i in range(1, A+1):
#>    B = B + i
#>print(B)





# 15552번
#>import sys

#>Test_num = int(sys.stdin.readline())
# 정수를 입력 받을 땐 int로 형변환을 거치면 개행문자 제거와 정수형 변환을 동시에 할 수 있다.
# 문자열 하나를 받을 거면 readline().strip() 해주기
#>input_list = []
#>input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(Test_num)]
#>for i in range(Test_num):
#>    print(sum(input_list[i]))




# 2741번
#>import sys
#>Test_num = int(sys.stdin.readline())
#>for i in range(1, Test_num + 1):
#>    print(i)






# 2742번
import sys
Test_num = int(sys.stdin.readline())
for i in range(Test_num, 0, -1):
    print(i)