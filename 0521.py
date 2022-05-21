# 22년 5월 21일 백준 알고리즘 풀이

# 1330번
# A, B = input().split(" ")
# A = int(A)
# B = int(B)
# int(input().split(" ")는 오류를 발생시킨다. 리스트를 정수형으로 바꿀 수 없기 때문이다.
# map 함수도 사용해보자

# if A < B:
#     print("<")
# elif A > B:
#    print(">")
# else:
#     print("==")

# 9498번
# A = int(input())
# input()은 하나만 받는 것이므로 int 함수로 바로 변형 해줄 수 있다.
# if A >= 90:
#     print("A")
# elif 89 >= A and A >= 80:
#     print("B")
# elif 79 >= A and A >= 70:
#     print("C")
# elif 69 >= A and A >= 60:
#     print("D")
# else:
#     print("F")

# 2753번
# A = int(input())
# C1 = int((A % 4)==0)
# Calculation 1의 약자
# C2 = int((A % 100)==0)
# C3 = int((A % 400)==0)
# 윤년 계산을 위해 나머지를 구해야 했는데 if 문에서 구하면 코드가 길어지므로 먼저 한다.
# 정수형으로 바꾸면 사칙연산 등을 통해 여러 조건을 한번에 검증할 수 있을 것 같아서 정수형으로 변환했다.
# if C1 - C2 == 1:
#     print("1")
# elif C3 == 1:
#     print("1")
# else:
#     print("0")


# 14681번
# s_list = [input() for _ in range(2)]
# 엔터 구분 입력
# A = int(s_list[0])
# B = int(s_list[1])
# if문을 중첩으로 쓰는 게 중첩으로 쓰지 않는 것보다 간단할 거라고 판단했다.
# if A * B > 0:
#     if A > 0:
#         print("1")
#     else:
#         print("3")
# else:
#     if A > 0:
#         print("4")
#     else:
#        print("2")

# 2884번

# A, B = map(int, input().split())
# map 함수로 입력 받는 값을 정수로 변환하는 걸 한 줄로 만들었다.
# C1 = (B - 45) >= 0

# if C1 == False:
#     if A == 0:
#         A = A + 24 - 1
#     else:
#        A = A - 1
#    B = B + 60 - 45
    # 이해를 돕기 위해 15가 아닌 60 - 45라고 표기했다.
#    print('{0} {1}'.format(A, B))
# else:
#     B = B - 45
#     print('{0} {1}'.format(A, B))

# 오늘 배운 것 중 메모
# 입력 형태
# A, B = map(int, input().split())
# 출력 형태
# print('{0} {1}'.format(A, B))
