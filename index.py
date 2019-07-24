# 클래스란 설계도와 같고, 인스턴스는 제품과 같다.
# class 선언 방법
# class 클래스 이름:
#   변수의 정의
#   함수의 정의

class fruit:
    color = 'red'
    def taste(self): # 클래스에서 함수를 정의할 때는 이 self를 반드시 적어야 한다.
        return 'delicious'

# 클래스의 인스턴스화
apple = fruit()
print(apple.color)
print(apple.taste())

# 객체란? 데이터와 메소드가 묶인 것
# 파이썬에서 객체는 데이터형이라 바꿔 말할 수 있다.

color = 'green'
print(color.count('e'))
# 여기에서 color가 객체고, count가 메소드이다.

# 요약
# 객체는 데이터와 기능(메소드)을 가진다.
# 데이터형도 데이터와 메소드를 가지므로 객체다.
# 클래스는 데이터와 메소드에 대한 설계도이고, 설계도(클래스)로 제품을 제작하면 객체가 된다.

class staff:
    bonus = 30000
    def salary(self): # 함수의 제 1인자로 자동으로 전달되는 것은 클래스 자신이다.
        salary = 10000 + self.bonus # 클래스에서의 변수를 함수에서 쓰려면 self 필요
        return salary
kim = staff()
print(kim.salary())

# __init__ 메소드: 초기 설정값
# class 클래스 이름:
#   def __init__(self, 인자..):
#       self.초기 설정하고 싶은 변수 = 인자
#       초기 수행 처리
#   def 메소드 이름:
#       메소드 처리

class staffs:
    def __init__(self, bonus):
        self.bonus = bonus
    def salary(self):
        salary = 100000 + self.bonus
        return salary

kims = staffs(50000)
print(kims.salary())


class staffInfo:
    def __init__(self, staff_id):
        self.staff_id = staff_id
    def getWorkingHours(self):
        if (self.staff_id == 'A00122'):
            return '50hours'
        # 사원의 근무 시간을 관리하는 DB에서 self.staff_id를 바탕으로 정보를 취득
    def getHireDate(self):
        if(self.staff_id == 'A00122'):
            return '2015-11-29'
        # 사원의 채용 계약 정보를 관리하는 DB에서 self.staff_id를 바탕으로 정보를 취득
    def getTrainingRank(self):
        if(self.staff_id == 'A00122'):
            return 'Beginner'
        # 사원의 연수 정보를 관리하는 DB에서 self.staff_id를 바탕으로 정보를 취득
    
kim = staffInfo('A00122') # 사원 번호를 초깃값으로 인스턴스화
print(kim.getWorkingHours())
print(kim.getHireDate())
print(kim.getTrainingRank())