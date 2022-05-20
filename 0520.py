# 220520 백준 알고리즘 풀이

# 10926번
# A = input()
# print(A+"??!")
# +로 문자열을 합칠 수 있다.

# 18108번
# A = input()
# print(int(A)-543)

# 10430번
# A, B, C = input().split(" ")
# A = int(A)
# B = int(B)
# C = int(C)
# print((A+B)%C)
# %는 나머지 구하는 연산자
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

# 2588번
# A, B = input().split(" ")
s_list = [input() for _ in range(2)]
# 여러 줄 입력 받을 때는 for _ in range(n)을 사용한다.
# 리스트 안에 input을 받는데 for _ int range(n)로 반복문이 걸린다.
L1 = int(s_list[0]) * int(s_list[1][2])
L2 = int(s_list[0]) * int(s_list[1][1])
L3 = int(s_list[0]) * int(s_list[1][0])
L4 = L1 + (L2*10) + (L3*100)
print(L1)
print(L2)
print(L3)
print(L4)
