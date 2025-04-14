<<<<<<< HEAD
import socket

HOST = '127.0.0.1'
PORT = 8747

sock = socket.socket()

def init(nickname) -> str:
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}'

        return submit(init_command)

    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')
        print(e)


def submit(string_to_send) -> str:
    try:
        sock.send((string_to_send + ' ').encode('utf-8'))

        return '[RESULT] test ok'

    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')

    return None


def close():
    try:
        if sock is not None: sock.close()
        print('[STATUS] Connection closed')

    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')


NICKNAME = '통신테스트'
game_data = init(NICKNAME)

# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 수신 데이터 출력
    print(f'{game_data}\n')

    # 커맨드 지정
    output = 'A'

    # 커맨드 전송
    game_data = submit(output)

    # 강제 종료(통신테스트용)
    break

# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()
=======
import sys
sys.stdin = open("2.txt", "r")

tc = int(input())
T = int(input())
result = ""
for _ in range(T):
    arr = input().split()
    n = int(arr[1])
    result += arr[0] * n
print(result)
for i in range(len(result)//10):
    scope = result[0:i]
    print(scope)
>>>>>>> 3fa5eee063b781d215dc44d9c691a7c82afc1765
