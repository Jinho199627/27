# 2022년 05월 26일 백준 알고리즘 풀이
import sys


# 15596번 (문제 잘 읽고 풀자.)
#>def solve(a):
#>    return sum(a)




# 4673번
#>answer_list = list(range(1,10001))
#>for i in answer_list:
#>    d = i
#>    while True:
#>        mid_cal = []
#>        for l in str(d):
#>            mid_cal.append(int(l))
#>        d = d + sum(mid_cal)
#>        try:
#>            answer_list.remove(d)
#>        except:
#>            break            
#>for i in answer_list:
#>    print(i)
#(배운 것) 처음 while에는 들어가야 하고 중간에 나와야 한다면 try except 구문을 사용해보자
#(배운 것) while 안의 except에서 break해주면 딱 while 구문 밖으로만 나온다.



# 1065번
N = int(sys.stdin.readline())
for i in range(1,N+1):
    check_list = []
    for l in str(i):
        check_list.append(int(l))
    print(check_list)