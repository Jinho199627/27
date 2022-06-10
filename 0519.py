# 백준 알고리즘 풀이 5월 19일

# 1001번
# 코드 A, B = input().split( )
# A와 B 변수는 input 값으로 받고 구분 기호는 공백이다.
# 코드 print(int(A)-int(B))
# input으로 받은 변수는 문자형이라서 int로 형태 변환 해준다.

# 10998번 (input 형태만 기억하고 int로 바꿔준다면 쉽게 코드를 짤 수 있다.)
# A, B = input().split( )
# print(int(A)*int(B))

# 1008번
# A, B = input().split( )
# print(int(A)/int(B))

# 10869번(몫과 나머지는 함수를 쓰는 게 좀 더 직관적인 이해가 가능할 것 같아서 함수를 사용했다.)
A, B = input().split( )
print(int(A)+int(B))
print(int(A)-int(B))
print(int(A)*int(B))
print(divmod(int(A), int(B))[0])
# print(int(int(A)/int(B)))
print(divmod(int(A), int(B))[1])
# print(int(A)%int(B))
# divmod(A, B) = (몫, 나머지)
