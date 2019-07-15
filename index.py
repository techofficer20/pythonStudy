# 수치형
# 1, 2, 10과 같은 숫자를 다루는 데이터형
# 수치형 데이터끼리는 더하기, 빼기 등의 연산 가능
# 숫자를 문자열로 다루는 경우도 있는데, 이때는 산술적인 의미에서 더하거나 뺄 수 없다.
# 종류1: 정수형 (int)
a = 34 + 56
print(a)  # 90
number = 55
# 종류2: 부동소수점(소수) (float)
a = 5 + 3.4
print(a)  # 8.4
a = 5 / 2
print(a)  # 2.5
# 종류3: 복소수 (complex)
complex = 5 + 5j
print(complex + (3 + 1j))  # 8 + 6j

# 문자열형
# 문자열을 다루는 데이터형
# 문자들을 작은 따옴표 혹은 큰따옴표로 둘러싸서 문자열형을 지정할 수 있다.
# 작은따옴표 혹은 큰따옴표를 세 개 연속하여 붙이면 복수행의 문자열을 만들 수 있다.
message = 'happy birthday!!'
print(message)
message = "축하합니다!"

# 문자열형과 산술연산자
# +를 사용한 문자열 조작
message = 'thunder' + 'bolt'
print(message)  # thunderbolt

# *을 사용한 문자열 조작
message = 'hunter' * 2
print(message)  # hunterhunter

# 문자열형의 편리한 기능
# upper() : 전부 대문자로 바꿈
text = 'hello'
print(text.upper())  # HELLO
# count(): 지정한 문자가 몇 개 있는지 셈

word = 'maintenance'
print(word.count('n'))  # 3

# 이렇게 데이터형이 가지는 기능을 메소드라고 한다.

# 논리형
print(46 < 49)  # True
print(46 > 49)  # False

# 리스트형
# 묶고 싶은 데이터를 쉼표로 구분하여 대괄호에 넣는다.
Agroup = ['lee', 'kim']
print(Agroup)  # ['lee', 'kim']
Agroup.append('park')  # 요소 추가
print(Agroup)  # ['lee', 'kim', 'park']
Agroup.remove('kim')  # 요소 제거
print(Agroup)  # ['lee', 'park']
Agroup = ['lee', 'kim', 'park']
Agroup.sort()  # 알파벳 순서대로 정렬
print(Agroup)  # ['kim', 'lee', 'park']
test_result = [87, 55, 99, 50, 66, 78]
test_result.sort()  # 오름차순 정렬
print(test_result)
# 정렬 시 주의: 수치형 데이터와 문자열형 데이터가 섞여 있으면 에러 발생함. 동일한 데이터형만 담는다.

# 사전형
# 색인(key)과 데이터(value)를 묶어서 독자적인 사전을 구성하는 식
activities = {'Monday': '농구', 'Tuesday': '자전거',
              'Wednesday': '밴드', 'Friday': '수영'}
print(activities['Tuesday'])  # 자전거
print(activities.keys()) # dict_keys(['Monday', 'Tuesday', 'Wednesday', 'Friday'])
print(activities.values())  # dict_values(['밴드', '수영', '자전거', '농구'])

# 튜플형
# 복수의 요소를 쉼표로 구분하여 소괄호로 감싼 것
# 만든 후 바꿀 수 없다.
# 새로운 요소를 추가하는 것이 지원되지 않는다.
# 사전형 데이터의 키로 사용될 수 있다.

tuple_sample = ('apple', 3, 90.4)
print(tuple_sample) # ('apple', 3, 90.4)

diary = {}
key = ('katana', '08-01')
diary[key] = '70kg'
print(diary) # {('katana', '08-01'): '70kg'}

# 사전의 키로 튜플형은 사용할 수 있지만, 리스트형은 사용할 수 없다.
# 사전형 데이터의 키는 변경할 수 없는 데이터형만 등록할 수 있기 때문. 사전의 키가 자주 변경되면 좋지 않기 때문.
# 튜플형을 사용하면 복수의 데이터를 조합해서 키를 설정할 수 있다.

# 집합형
# 리스트형이나 튜플형처럼 복수의 데이터를 하나로 묶어서 다루는 것이 가능한 데이터형이다.
# 사전형과 같이 중괄호를 사용하여 리스트형이나 튜플형처럼 요소를 나열하여 정의한다.

candy = {'delicious', 'fantastic'}
print(candy) # {'delicious', 'fantastic'}
# Set 함수를 사용하여 집합형 데이터를 만들 수도 있다.
candy = set('delicious')
print(candy) 
# 한 글자씩 순서 랜덤으로 출력됨 (집합형 데이터는 순서를 저장하지 않는다.)
# 중복되는 데이터를 가지지 않는다.
# 한 글자씩 분리되는 것을 막으려면 리스트형에 정리한 후 set에 전달하면 된다.
flavor = ['apple', 'peach', 'soda']
candy = set(flavor)
print(candy) # apple, peach, soda가 순서 랜덤으로 출력
candy.update(['grape']) # 집합형 요소 추가 (리스트형으로)
print(candy) # apple, peach, soda, grape가 순서 랜덤으로 출력
# 중복된 데이터를 없애고 싶다면? 리스트형의 데이터를 집합형으로 변환하고 다시 리스트형으로 변환하는 방법을 사용한다.
flavor = ['apple', 'soda', 'chocolate', 'apple', 'grape', 'grape', 'soda']
flavor_set = set(flavor) 
print(flavor_set) # apple, soda, grape, chocolate 순서 랜덤으로 출력
flavor = list(flavor_set)
print(flavor) # apple, soda, grape, chocolate 순서 랜덤으로 출력
# 복수 데이터 간의 계산
flavor_set_A = {'apple', 'peach', 'soda'}
flavor_set_B = {'apple', 'soda', 'chocolate'}
print(flavor_set_A - flavor_set_B) # peach
print(flavor_set_A & flavor_set_B) # apple, soda