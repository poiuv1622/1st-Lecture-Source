import pyautogui
import time

# 각 요소의 좌표를 직접 측정하여 입력하세요!
start_year_pos = (969, 677)   # 시작년도 클릭 위치
start_month_pos = (1067, 681)  # 시작월 클릭 위치
end_year_pos = (1235, 678)     # 종료년도 클릭 위치
end_month_pos = (1352, 678)    # 종료월 클릭 위치
search_btn_pos = (1411, 913)   # 검색버튼 클릭 위치
download_btn_pos = (1457, 971) # 엑셀다운로드 버튼 위치

time.sleep(2) # 시작 전 준비 시간

def year_click(year):
    # 1. 시작 년도 클릭 및 입력
    pyautogui.click(*start_year_pos)
    time.sleep(2.0)
    pyautogui.write(year)
    pyautogui.press('enter')
    time.sleep(2.0)

    # 3. 종료 년도 클릭 및 입력
    pyautogui.click(*end_year_pos)
    time.sleep(2.0)
    pyautogui.write(year)
    pyautogui.press('enter')
    time.sleep(2.0)

def month_click(start_m, end_m):

    # 2. 시작 월 클릭 및 입력
    pyautogui.click(*start_month_pos)
    time.sleep(2.0)
    pyautogui.write(start_m)
    pyautogui.press('enter')
    time.sleep(2.0)

    # 4. 종료 월 클릭 및 입력
    pyautogui.click(*end_month_pos)
    time.sleep(2.0)
    pyautogui.write(end_m)
    pyautogui.press('enter')
    time.sleep(2.0)

def download():
    # 5. 검색 버튼 클릭 후 대기
    pyautogui.click(*search_btn_pos)
    time.sleep(5) # 데이터 로딩 대기

    # 6. 엑셀 다운로드 클릭 + 엔터 + 대기
    pyautogui.click(*download_btn_pos)
    time.sleep(2.0)
    pyautogui.press('enter')
    time.sleep(5) # 다운로드 대기

years = ['2023', '2024', '2025']

month_pair = [('01','06'),('07','12')]

for year in years :

    time.sleep(3)

    year_click(year)
    for start_m, end_m in month_pair:

        month_click(start_m, end_m)

        download()



print("매크로 완료")
