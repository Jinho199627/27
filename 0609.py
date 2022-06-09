# 파이썬 실행파일 만드는 방법
 
# 파이썬이 설치되지 않은 컴퓨터에 프로그램 배포
# 라이브러리 pyinstaller
print("Hello startcoding")
input() # 프로그램이 꺼지지 않도록 인풋 창 열기

# 이런 파일 만들고
# 터미널 창에서
# C:\jocoding>pip install pyinstaller
# 설치 완료되면
# C:\jocoding>pyinstaller 0609.py 입력(경로 입력)


# build 폴더
# 방금 실행파일을 만들 때 필요한 파일이 들어있는 폴더

# dist 폴더
# 방금 만든 0609.py 파일이 작동할 때 같이 있어야 하는 파일들

# spec 파일
# 실행 파일을 만들 때 사용할 옵션 파일





# 하나의 실행파일로 만들기
# 실행 파일 만드려는 위치로 가서 아래 명령어 입력
# pyinstaller -F (실행파일로 만들려는 파일명).py
# pyinstaller -F 0609.py