# if, else 문
age = 29
if(18 <= age):
    print('티켓을 판다')
else:
    print('티켓을 팔 수 없습니다')

# if, else if, else 문 (위에서부터 차례대로 되기 때문에, 순서 중요)
age = 60
if(60 <= age):
    print('티켓은 5000원 입니다.')
elif(18 <= age):
    print('티켓은 8000원 입니다.')
else:
    print('티켓을 판매할 수 없습니다.')

pointCard = True
count = 5
if(pointCard == True):
    if(count == 5):
        print('감사합니다. 이번 편은 5000원으로 감상할 수 있습니다.')

if(pointCard == True and count == 5):
    print('감사합니다. 이번 편은 5000원으로 감상할 수 있습니다.')

if(pointCard == True or count == 5):
    print('감사합니다. 이번 편은 5000원으로 감상할 수 있습니다.')