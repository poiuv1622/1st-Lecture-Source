import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f"현재 마우스 좌표: x={x}, y={y}", end='\r')  # 줄 바뀌지 않고 출력
        time.sleep(0.1)  # 0.1초마다 갱신
except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")

