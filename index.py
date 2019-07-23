# for를 사용, 정해진 횟수만큼 반복 처리를 실시
# for 변수 in range(반복하고 싶은 횟수):
#   반복하고 싶은 처리(변수에는 0에서부터 숫자가 대입됨)
for count in range(3):
    print('반복하기')
    print(count)

word = 'ninja'
for chara in word:
    print(chara)

# 리스트형의 각 데이터에 대해 같은 처리를 수행하고 싶을 때
# for 변수 in 리스트형:
#   반복하고 싶은 처리(변수에는 리스트의 각 요소가 대입됨)
music_list = ['DEATH METAL', 'ROCK', 'ANIME', 'POP']
for music in music_list:
    print('now playing...' + music)

# 사전형 데이터의 요소별로 같은 처리를 수행하고 싶을 때
# for 변수 in 사전형:
#   반복하고 싶은 처리(변수에는 사전의 키가 대입됨)
menu = {'라면':500, '김밥':430, '만두':210}
for order in menu:
    print(order) # 변수 order에 들어가는 데이터는 사전형 데이터가 아니라 사전의 키이다.
    print(menu[order] * 1.08)

# while을 사용하고 정해진 조건 동안 반복 처리를 실시
# while(조건식):
#   반복하고 싶은 처리
#   조건 갱신
counter = 0
while(counter < 5):
    print(counter)
    counter = counter + 1 # 무한루프는 조건 갱신 X

# 도중에 처리를 종료
# 반복문 안에서 break
while(True):
    print('주먹')
    print('발차기')
    break
    print('필살비법')

# 도중에 처리를 넘기고 싶을 때
# 반복문 안에서 continue
family = ['ryu-ko', 'mako', 'satsuki']
for kid in family:
    print('Good Morning! ' + kid)
    print('Wake up')
    print('breakfast')
    continue # 처음으로 되돌아감
    print('Go to School')