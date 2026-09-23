import streamlit as st
import random
import time

# 메뉴 데이터
menus = {
    "한식": ["떡볶이", "김치찌개", "된장찌개", "부대찌개", "제육볶음", "국밥", "삼겹살", "곱창", "닭갈비", "찜닭", "비빔밥", "불고기", "감자탕", "뼈해장국", "육회"],
    "양식": ["파스타", "피자", "스테이크", "리조또", "햄버거"],
    "중식": ["마라탕", "짜장면", "짬뽕", "탕수육", "볶음밥", "깐풍기", "양꼬치", "훠궈"],
    "일식": ["초밥", "돈까스", "라멘", "우동", "규동", "소바", "텐동", "연어덮밥", "가츠동", "오코노미야키", "타코야키", "야끼토리", "카레", "샤브샤브", "사케동"],
    "기타": ["쌀국수", "타코", "팟타이", "케밥", "커리", "반미", "퀘사디아", "마라샹궈"]
}

# 페이지 설정
st.set_page_config(page_title="저녁 메뉴 추천", page_icon="🍽️")

st.title("🍽️ 오늘 저녁 뭐 먹지?")
st.write("원하는 종류를 선택하면 랜덤으로 메뉴를 추천해 드립니다.")
st.markdown("---")

# 체크박스 UI 레이아웃 구성
st.subheader("✅ 카테고리 선택")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    kr = st.checkbox("한식", value=True)
with col2:
    we = st.checkbox("양식")
with col3:
    cn = st.checkbox("중식")
with col4:
    jp = st.checkbox("일식")
with col5:
    etc = st.checkbox("기타")

st.markdown("---")

# 추천 버튼
if st.button("🎲 메뉴 추천받기", use_container_width=True):
    selected_menus = []
    
    if kr: selected_menus.extend(menus["한식"])
    if we: selected_menus.extend(menus["양식"])
    if cn: selected_menus.extend(menus["중식"])
    if jp: selected_menus.extend(menus["일식"])
    if etc: selected_menus.extend(menus["기타"])

    if not selected_menus:
        st.warning("⚠️ 최소 한 가지 이상의 카테고리를 선택해주세요!")
    else:
        with st.spinner("맛있는 메뉴를 고르는 중..."):
            time.sleep(1) # 룰렛을 돌리는 듯한 짧은 대기 시간
            chosen = random.choice(selected_menus)
            
        st.success(f"🎉 오늘의 추천 메뉴는 **[{chosen}]** 입니다! 🎉")
        st.balloons() # 풍선 애니메이션 효과