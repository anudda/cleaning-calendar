import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정: 가로를 넓게 쓰고 메뉴바를 숨겨서 깔끔하게 만듭니다.
st.set_page_config(page_title="서비스 일정표", layout="wide")

# 사이트 제목
st.title("🗓️ 서비스 일정표")

# 질문자님의 캘린더 ID를 기반으로 만든 임베드 주소
# ctz=Asia/Seoul: 한국 시간 기준
# wkst=1: 월요일 시작 (일요일 시작을 원하시면 7로 변경)
# bgcolor: 배경색 흰색
calendar_url = "https://calendar.google.com/calendar/embed?src=c2cc4f87918756f0f37702053abac637c49edcdab47716a3231a431503ea5933%40group.calendar.google.com&ctz=Asia%2FSeoul&wkst=1&bgcolor=%23ffffff&showTitle=0&showNav=1&showPrint=0&showTabs=0&showCalendars=0&showTz=0"

# iframe을 사용하여 달력을 화면에 꽉 차게 띄웁니다.
# 모바일에서 보기 편하도록 높이를 600~700 정도로 설정합니다.
calendar_html = f"""
    <iframe src="{calendar_url}" 
    style="border: 0" width="100%" height="600" frameborder="0" scrolling="no">
    </iframe>
"""

# 화면 출력
components.html(calendar_html, height=650)

st.divider()
st.info("💡 캘린더에 적힌 시간을 누르면 상세 내용을 보실 수 있습니다.")
