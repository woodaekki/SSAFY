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
