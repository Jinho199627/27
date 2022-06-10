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



# 1065번 (푸는 중)
def number(a):
    check_list = []
    check_set = set()
    for i in str(a):
        check_list.append(int(i))
    for m in range(len(check_list)):
        try:
            check_set.add(check_list[m]-check_list[m+1])
        except:
            break
    if len(check_set) <= 1:
        answer = 1
    else:
        answer = 0
    return answer
#(배운 것) try except 구문은 매우 유용하다. 오류 처리를 해주니 구문을 조금 더 자유롭게 짤 수 있다.


N = int(sys.stdin.readline())
box = 0
for k in range(1,N+1):
    if number(k) == 1:
        box = box + 1
print(box)
#(배운 것) 함수를 만들어두면 향후 코드 구축이 쉽다.
