# 함수 생성 방법
# def 함수의 이름():
#   처리 1
#   처리 2

def washingMachine(mode):
    print('급수한다')
    if(mode == 'soft'):
        print('부드럽게 씻는다')
    elif(mode == 'hard'):
        print('세게 씻는다')
    else:
        print('씻는다')
    print('헹군다')
    print('탈수한다')
    print('건조한다')

mode = 'soft'
washingMachine(mode)

# 데이터를 반환하는 함수
def area(radius):
    result = radius * radius * 3.14
    return result

print(area(5))

# 내장 함수
# len(): 인자로 전달한 데이터의 길이나 요소의 수를 반환함
animal = ['cat', 'dog', 'duck']
print(len(animal))
# max(): 인자로 전달한 데이터 중에서 가장 큰 값을 반환
print(max(100, 10, 50))
print(max('thunderbolt')) # 알파벳 z에 가장 가까운 문자
# min(): 인자로 전달한 데이터 중에서 가장 작은 값을 반환
print(min(300, 30, 3000))
print(min('thunderbolt')) # 알파벳 a에 가장 가까운 문자

print(min('1Aa')) # 1 
print(max('1Aa')) # a
# 숫자 > 알파벳 대문자 > 알파벳 소문자 순으로 크기를 계산

# sort(): 전달한 데이터를 정렬하여 리스트형으로 변환하는 함수 (무작위)
print(sorted('thunderbolt')) 

# print(): 출력을 위해 사용

# type(): 조사하고 싶은 데이터나 변수를 전달하면 데이터 타입을 반환
hatena_1 = 9800
print(type(hatena_1))

# dir(): 어떤 메소드가 있는지 잊어버렸을 때 사용
string = 'hey'
print(dir(string))
# 그냥 dir()은 dir이 실행된 시점에서 유효한 변수의 목록이 나타남
print(dir())