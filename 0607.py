# 2022년 06월 07일 클래스 상속 공부

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

# 클래스의 상속은 다른 클래스를 만들 때 기존 클래스의 기능을 물려받을 수 있는 기능이다.
# 상속을 통해 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경할 수 있다.
class MoreFourCal(FourCal):
    # 상속받을 클래스 이름을 괄호 안에 넣어준다.
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
print(a.mul())
# 8로 정상 작동이 되는 걸 확인
print(a.pow())



a = FourCal(4,0)
# print(a.div())
# 이러면 div zero 오류가 나온다.

# 클래스의 오류 예방
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return "DivZero"
        else:
            return self.first / self.second
c = SafeFourCal(4,0)
print(c.div())




class Family:
    last_name = "김"

print(Family.last_name)
# 클래스를 호출하고 클래스 내부의 last_name을 불러온다.

d = Family()
e = Family()
print(d.last_name)
print(e.last_name)
# 앞서 d와 e를 Family Class로 지정해주었으니 d와 e의 last_name을 불러올 수 있다.