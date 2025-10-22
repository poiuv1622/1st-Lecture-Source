import streamlit as st
import random
import time

# 식당별 메뉴 딕셔너리
restaurant_menus = {
    "팔용돼지국밥": ["돼지국밥", "수육"],
    "남도식당": ["생선구이", "된장찌개"],
    "한우명가 팔용점": ["한우 등심", "한우 불고기"],
    "김가네순두부": ["순두부찌개", "청국장"],
    "진미양푼갈비찜": ["양푼갈비찜", "제육볶음"],
    "팔용반점": ["짜장면", "짬뽕"],
    "홍콩반점": ["짬뽕", "탕수육"],
    "다마고회전초밥": ["연어초밥", "참치초밥"],
    "은하수초밥": ["모듬초밥", "회덮밥"],
    "팔용왕만두": ["왕만두", "쫄면"],
    "분식나라": ["떡볶이", "돈까스"],
    "팔용소금구이": ["소금구이", "삼겹살"],
    "명륜진사갈비 창원팔용점": ["LA갈비", "양념갈비"],
    "팔용칼국수": ["바지락칼국수", "수제비"],
    "팔용쌍둥이국수": ["잔치국수", "비빔국수"],
    "멜로우라운지": ["까르보나라", "고르곤졸라피자"],
    "아웃백스테이크하우스 창원점": ["토마호크 스테이크", "블루밍어니언"],
    "카페유니크": ["아메리카노", "티라미수"],
    "팔용커피공장": ["핸드드립커피", "버터스콘"],
    "팔용그릴치킨": ["숯불치킨", "양념치킨"],
}

restaurants = list(restaurant_menus.keys())

st.title("창원 현대위아 인근 랜덤 회식 장소 추천기")

if st.button("회식장소 추천받기"):
    with st.spinner('최고의 회식 장소를 찾는 중...'):
        time.sleep(1)  # 스피너 보이는 시간(1초)
        selected_restaurant = random.choice(restaurants)
        menus = restaurant_menus[selected_restaurant]
        menu_recommend = random.sample(menus, min(2, len(menus)))
        
    st.success(f"🎉 오늘의 회식 장소: **{selected_restaurant}**")
    st.write(f"추천 메뉴: {', '.join(menu_recommend)}")
    st.balloons()
