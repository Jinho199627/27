# 22년 5월 22일 백준 알고리즘

# 2525번(앞으로 원래 코드였던 것들은 #> 이걸로 표기하기로 했다. 나중에 #>를 지우면 되기 때문.)
#> A, B = map(int, input().split(" "))
# A: 입력 시간
# B: 입력 분
#> C = int(input())
# C: 추가 시간


#> if B + C >= 60:
#>     M = divmod(B + C, 60)[1]
    # 출력 분을 나타내는 변수 M
    # B + C 값을 60으로 나눈 나머지가 출력 분이 된다.
#>     if A + divmod(B + C, 60)[0] >= 24:
        # 입력 시간과 추가 시간의 값이 24보다 커지면으로 두는 게 확실한 알고리즘이다.
#>         H = A + int(divmod(B + C, 60)[0]) - 24
        # 출력 시간을 나타내는 변수 H
#>     else:
#>         H = A + int(divmod(B + C, 60)[0])
#>  else:
#>     M = B + C
#>     H = A

#> print('{0} {1}'.format(H, M))

# 이 문제에서 배운 것은 24진수나 60진수 등으로 표현되는 건 되도록 상수 조건을 설정하지 말고
# 여러 가능성을 생각해서 변수를 활용한 조건을 세워야 한다는 것이다.





# 2480번
#> input_list = map(int, input().split(" "))
# 이 상태에서 input_list는 map class이다.
#>input_list = list(input_list)
# 리스트를 받으려는 의도대로 되지 않았다면 list함수를 사용해 다시 한번 변환해준다.

#> A = []
# 처음 원소들을 넣을 A 리스트
#> B = []
# 중복 검증할 B 리스트

#> for i in input_list:
#>     if i not in A:
#>         A.append(i)
#>     else:
#>         B.append(i)
# 중복인 원소들을 분류하는 반복문 처리

#> if len(B) == 2:
#>     print(B[0] * 1000 + 10000)
#> elif len(B) == 1:
#>     print(B[0] * 100 + 1000)
#> else:
#>     print(max(A) * 100)


# 2739번



A = int(input())

for i in range(1, 10):
    print('{0} * {1} = {2}'.format(A, i, A*i))
