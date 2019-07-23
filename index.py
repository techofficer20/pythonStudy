# 예외 처리 방법
# try:
#   처리 A (에러가 발생할 수 있는 처리)
# except:
#   처리 B
# 처리 A에서 예외가 발생하면 그것을 붙잡아서 except 밑의 처리 B가 실행
try:
    prin('예외가 발생하는 처리')
except:
    print('예외를 붙잡았다')

# 주로 프로그램이 외부와 통신하는 경우에 사용함. (ex: 서버)

try:
    prin('a')
except Exception as e: 
    # Exception 타입의 예외를 잡아 변수 e에 대입
    # e 객체의 args에는 에러 메시지가 들어있다.
    # 애플리케이션 내에서는 직접적으로 e.args를 표시하기보다는 사용자에게 적절한 안내문구를 표시하는 것이 좋다.
    print(e.args)