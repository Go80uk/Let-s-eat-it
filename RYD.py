import streamlit as st
import random
import time

# 1. 메뉴 데이터
menus = {
    "한식": ["떡볶이", "김치찌개", "된장찌개", "부대찌개", "제육볶음", "국밥", "삼겹살", "곱창", "닭갈비", "찜닭", "비빔밥", "불고기", "감자탕", "뼈해장국", "육회"],
    "양식": ["파스타", "피자", "스테이크", "리조또", "햄버거"],
    "중식": ["마라탕", "짜장면", "짬뽕", "탕수육", "볶음밥", "깐풍기", "양꼬치", "훠궈"],
    "일식": ["초밥", "돈까스", "라멘", "우동", "규동", "소바", "텐동", "연어덮밥", "가츠동", "오코노미야키", "타코야키", "야끼토리", "카레", "샤브샤브", "사케동"],
    "기타": ["쌀국수", "타코", "팟타이", "케밥", "커리", "반미", "퀘사디아", "마라샹궈"]
}

# 2. 페이지 기본 설정 및 상태 관리
st.set_page_config(page_title="저녁 메뉴 룰렛", page_icon="🤮", layout="centered")

# 화면 전환을 위한 session_state 초기화 ('select' -> 'box' -> 'result')
if 'stage' not in st.session_state:
    st.session_state.stage = 'select'
if 'selected_menu' not in st.session_state:
    st.session_state.selected_menu = ""

# 3. 킹받는 CSS 강제 주입
st.markdown("""
<style>
    /* 눈 아픈 무지개 배경 & 궁서체 */
    .stApp {
        background: linear-gradient(45deg, #ff00ff, #00ff00, #ffff00, #00ffff, #ff0000);
        background-size: 500% 500%;
        animation: gradientBG 2s ease infinite;
        font-family: '궁서', 'Gungsuh', serif !important;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 킹받는 텍스트 색상 및 그림자 */
    h1, h2, h3, p, label {
        color: #ff0000 !important;
        text-shadow: 2px 2px 0px #ffff00, -2px -2px 0px #0000ff;
        font-weight: bold !important;
    }

    /* 버튼 발작 애니메이션 */
    .stButton > button {
        background-color: #00ff00 !important;
        color: #ff00ff !important;
        border: 5px dotted #ff0000 !important;
        border-radius: 50px !important;
        font-size: 25px !important;
        font-family: '궁서', 'Gungsuh', serif !important;
        font-weight: bold;
        transition: all 0.1s;
    }
    
    .stButton > button:hover {
        transform: scale(1.2) rotate(-5deg);
        background-color: #ffff00 !important;
        animation: shake 0.2s infinite;
    }

    @keyframes shake {
        0% { transform: translate(2px, 1px) rotate(0deg); }
        10% { transform: translate(-1px, -2px) rotate(-1deg); }
        20% { transform: translate(-3px, 0px) rotate(1deg); }
        30% { transform: translate(0px, 2px) rotate(0deg); }
        40% { transform: translate(1px, -1px) rotate(1deg); }
        50% { transform: translate(-1px, 2px) rotate(-1deg); }
        60% { transform: translate(-3px, 1px) rotate(0deg); }
        70% { transform: translate(2px, 1px) rotate(-1deg); }
        80% { transform: translate(-1px, -1px) rotate(1deg); }
        90% { transform: translate(2px, 2px) rotate(0deg); }
        100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    
    /* 체크박스 크기 키우기 */
    input[type="checkbox"] {
        transform: scale(2);
        margin: 10px;
    }
    
    /* 상자 버튼을 위한 특별한 클래스 처리 (스트림릿 꼼수) */
    div[data-testid="stButton"] {
        display: flex;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# [화면 1] 메뉴 선택 화면
# ==========================================
if st.session_state.stage == 'select':
    st.markdown("<marquee scrollamount='30'><h1>🍽️ 오 늘 저 녁 뭐 먹 지 🍽️</h1></marquee>", unsafe_allow_html=True)
    st.write("체크박스를 선택하고 버튼을 누르라능 ㅋ")
    
    # 체크박스 레이아웃
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: kr = st.checkbox("한식", value=True)
    with col2: we = st.checkbox("양식", value=True)
    with col3: cn = st.checkbox("중식")
    with col4: jp = st.checkbox("일식")
    with col5: etc = st.checkbox("기타")

    st.write("")
    st.write("")

    if st.button("🎲 당장 밥 내놔라 🎲", use_container_width=True):
        selected_menus = []
        if kr: selected_menus.extend(menus["한식"])
        if we: selected_menus.extend(menus["양식"])
        if cn: selected_menus.extend(menus["중식"])
        if jp: selected_menus.extend(menus["일식"])
        if etc: selected_menus.extend(menus["기타"])

        if not selected_menus:
            st.error("아무것도 안 고르면 굶어야지 ㅉㅉ")
        else:
            st.session_state.selected_menu = random.choice(selected_menus)
            st.session_state.stage = 'box'
            st.rerun() # 다음 화면으로 넘어가기 위해 리프레시


# ==========================================
# [화면 2] 선물 상자 화면 (box.cyhuh.com 느낌)
# ==========================================
elif st.session_state.stage == 'box':
    st.markdown("<h1 style='text-align: center;'>📦 택배 왔 다 능 📦</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>아래 상자를 냅다 클릭해보라능 ㅋ</h3>", unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # 거대한 상자 모양의 버튼 만들기
    if st.button("🎁\n\n(클릭)", use_container_width=True):
        st.session_state.stage = 'result'
        st.rerun()


# ==========================================
# [화면 3] 결과 화면
# ==========================================
elif st.session_state.stage == 'result':
    st.balloons() # 풍선 이펙트
    st.snow()     # 눈망울 이펙트 (난장판을 위해 추가)
    
    # 정신없이 움직이는 텍스트 (위아래로 튕김)
    st.markdown(f"""
    <marquee behavior="alternate" direction="up" scrollamount="40" style="height: 400px; text-align:center;">
        <marquee behavior="alternate" direction="left" scrollamount="40">
            <h1 style="font-size: 100px; line-height: 1.2;">
                🎉당첨🎉<br>
                {st.session_state.selected_menu}
            </h1>
        </marquee>
    </marquee>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    if st.button("🔄 마음에 안 들어? 다시 해 ㅋ", use_container_width=True):
        st.session_state.stage = 'select'
        st.session_state.selected_menu = ""
        st.rerun()
