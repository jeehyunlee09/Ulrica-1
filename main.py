import streamlit as st

# 1. 페이지 설정 (아이콘, 타이틀)
st.set_page_config(page_title="MBTI 진로 탐색 🚀", page_icon="✨", layout="wide")

# 2. 화려한 스타일을 위한 CSS 적용
st.markdown("""
    <style>
    /* 전체 배경 그라데이션 */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* 제목 스타일 */
    .main-title {
        font-size: 50px;
        font-weight: 800;
        color: #4A90E2;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    
    /* 카드 형태의 결과창 */
    .stAlert {
        border-radius: 20px;
        border: none;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    /* 버튼 커스텀 */
    div.stButton > button:first-child {
        background-color: #4A90E2;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #357ABD;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. MBTI 데이터 정의
mbti_data = {
    "ISTJ": {"emoji": "📏", "trait": "청렴결백한 논리주의자", "jobs": ["회계사", "공무원", "법률 전문가", "데이터 분석가"]},
    "ISFJ": {"emoji": "🛡️", "trait": "용감한 수호자", "jobs": ["간호사", "초등교사", "사회복지사", "사서"]},
    "INFJ": {"emoji": "🔮", "trait": "선의의 옹호자", "jobs": ["상담심리사", "작가", "환경운동가", "인사관리자"]},
    "INTJ": {"emoji": "🧠", "trait": "용의주도한 전략가", "jobs": ["경영 컨설턴트", "소프트웨어 개발자", "과학자", "투자 분석가"]},
    "ISTP": {"emoji": "🛠️", "trait": "만능 재주꾼", "jobs": ["엔지니어", "조종사", "프로그래머", "응급구조사"]},
    "ISFP": {"emoji": "🎨", "trait": "호기심 많은 예술가", "jobs": ["디자이너", "화가", "음악가", "조경가"]},
    "INFP": {"emoji": "📝", "trait": "열정적인 중재자", "jobs": ["예술가", "에디터", "심리치료사", "비영리단체 활동가"]},
    "INTP": {"emoji": "🔭", "trait": "논리적인 사색가", "jobs": ["대학교수", "연구원", "전략 기획자", "보안 전문가"]},
    "ESTP": {"emoji": "⚡", "trait": "모험을 즐기는 사업가", "jobs": ["기업가", "스포츠 매니저", "마케팅 전문가", "소방관"]},
    "ESFP": {"emoji": "🎭", "trait": "자유로운 영혼의 연예인", "jobs": ["연예인", "이벤트 플래너", "승무원", "홍보 전문가"]},
    "ENFP": {"emoji": "🌈", "trait": "재기발랄한 활동가", "jobs": ["크리에이티브 디렉터", "홍보 컨설턴트", "저널리스트", "카피라이터"]},
    "ENTP": {"emoji": "💡", "trait": "뜨거운 논쟁을 즐기는 변론가", "jobs": ["변호사", "광고 기획자", "정치인", "기업 경영인"]},
    "ESTJ": {"emoji": "📋", "trait": "엄격한 관리자", "jobs": ["프로젝트 매니저", "은행원", "군 장교", "행정관"]},
    "ESFJ": {"emoji": "🤝", "trait": "사교적인 외교관", "jobs": ["호텔리어", "초등교사", "홍보 담당자", "고객 서비스 매니저"]},
    "ENFJ": {"emoji": "📣", "trait": "정의로운 사회운동가", "jobs": ["교사", "외교관", "정치인", "라이프 코치"]},
    "ENTJ": {"emoji": "👑", "trait": "대담한 통치자", "jobs": ["CEO", "경제 분석가", "경영 컨설턴트", "변호사"]}
}

# 4. 메인 화면 구성
st.markdown('<h1 class="main-title">✨ 나의 MBTI 맞춤 진로 탐색 ✨</h1>', unsafe_allow_html=True)
st.write("<h3 style='text-align: center; color: #666;'>당신의 성격 유형 속에 숨겨진 완벽한 직업을 찾아보세요! 🚀</h3>", unsafe_allow_html=True)
st.markdown("---")

# 레이아웃 나누기
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    selected_mbti = st.selectbox(
        "나의 MBTI를 선택해 주세요 👇",
        options=list(mbti_data.keys()),
        index=0
    )
    
    find_btn = st.button("내 직업 추천받기! 🔍")

# 5. 결과 출력
if find_btn:
    # 효과 추가
    st.balloons()
    
    data = mbti_data[selected_mbti]
    
    st.markdown(f"""
        <div style="background-color: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center;">
            <h1 style="font-size: 80px; margin: 0;">{data['emoji']}</h1>
            <h2 style="color: #4A90E2;">{selected_mbti} : {data['trait']}</h2>
            <hr>
            <h4 style="color: #333;">추천하는 직업군 💼</h4>
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 20px;">
                {" ".join([f'<span style="background-color: #E1F5FE; padding: 10px 20px; border-radius: 50px; font-weight: bold; color: #01579B;"># {job}</span>' for job in data['jobs']])}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.info(f"💡 {selected_mbti} 유형은 자신의 강점을 살릴 수 있는 분야에서 가장 큰 보람을 느낍니다. 위 직업들을 함께 탐색해볼까요?")

# 6. 하단 푸터
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>© 2026 MBTI Career Education Program | Made with ✨ Streamlit</p>", unsafe_allow_html=True)
