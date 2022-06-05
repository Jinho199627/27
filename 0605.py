# 2022년 06월 05일 클래스 공부
import sys

# 클래스를 사용하는 이유는 전역변수와 함수를 무분별하게 찍어내는 걸 방지하기 위함이다.
# 그리고 코드를 수정할 때 효율적으로 변경할 수 있다.
# 클래스는 과자를 찍어내는 틀과 같다.

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator() # 먼저 만든 class로 별도의 계산기를 손쉽게 만든다.
cal2 = Calculator() # 별도의 계산기는 독립적인 값을 유지한다.

#>print(cal1.add(3))
#>print(cal1.add(4))
#>print(cal2.add(3))
#>print(cal2.add(7))

class FourCal:
    def __init__(self, first, second): # setdata와 큰 차이점은 없으나 객체 생성 시에 자동으로 호출된다는 차이가 있다. 
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
# self에는 a가 저장되고, 4는 first에 second는 2가 저장된다.
# a.first = 4
# a.second = 2

print(a.add())
print(a.div())

# b = FourCal()
# 이러면 에러 출력 왜냐하면 init에서 필요한 first와 second를 제공해주지 않았기 때문

b = FourCal(10,5)
print(b)