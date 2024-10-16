import streamlit as st

# CSS for changing the entire background color and styling the page
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

    /* Streamlit 전체 페이지의 배경을 변경하기 위한 설정 */
    .stApp {
        background-color: #020202;
        font-family: 'Nanum Gothic', sans-serif; /* Nanum Gothic 폰트 적용 */
        color: black; /* 기본 텍스트 색상 */
    }

    .full-width-banner {
        position: relative;
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://ifh.cc/g/tyYadc.jpg'); /* 반투명 검정색 오버레이와 이미지 */
        background-size: cover; /* 이미지 크기를 전체 영역에 맞춤 */
        background-position: center; /* 이미지 중앙 정렬 */
        height: 500px; /* 배너의 높이 설정 */
        width: 100vw; /* 페이지의 전체 너비를 사용 */
        margin-left: calc(-50vw + 50%); /* 페이지 중앙 정렬 후 왼쪽으로 이동 */
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        z-index: 1;
        flex-direction: column; /* 세로 방향 정렬을 위한 추가 */
    }

    /* 텍스트 스타일 */
    .full-width-banner h1 {
        font-size: 3em;
        margin: 0;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 텍스트에 그림자 추가 */
    }

    .centered-text {
        font-size: 1.5em;
        margin: 40px 0 20px 0; /* 위쪽에 40px, 아래쪽에 20px 마진 추가 */
        text-align: center; /* 텍스트 중앙 정렬 */
        color: white;
    }

    .centered-subtext {
        font-size: 1.2em;
        margin: 10px 0; /* 위쪽과 아래쪽에 10px 마진 추가 */
        text-align: center; /* 텍스트 중앙 정렬 */
        color: white;
    }

    /* 박스 스타일 */
    .box {
        background-color: #333333; /* 박스 배경색 */
        padding: 20px;
        border-radius: 7px;
        margin: 20px 0;
        color: white;
    }

    .box h3 {
        font-size: 1.2em;
        margin-bottom: 10px;
        text-align: left;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for the full-width banner and the centered texts below it
st.markdown(
    """
    <div class="full-width-banner">
        <h1>Welcome to team 예쁘DA</h1>
    </div>
    <div class="centered-text">
        반갑습니다. 오늘 어떤 하루를 보내고 계신가요?
    </div>
    <div class="centered-subtext">
        당신의 기분에 맞는 제주 맛집을 추천해드리겠습니다.
    </div>
    <div class="centered-subtext">
        추천을 위해 몇 가지 질문에 답해주세요.
    </div>
    """,
    unsafe_allow_html=True
)

# HTML for the box around the date input
st.markdown(
    """
    <div class="box">
        <h3>언제 방문하실 예정인가요?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# 날짜 입력 위젯 추가
selected_date = st.date_input("날짜를 선택하세요", help="맛집에 방문할 날짜를 선택해주세요.")

# 선택된 날짜 출력
st.write(f"선택한 날짜: {selected_date}")