import streamlit as st
from pathlib import Path
import tempfile

st.title("관리자 페이지")

CALL_FILE = Path(tempfile.gettempdir()) / "call.txt"

st.set_page_config(
    page_title="🍱 우리학교 급식 호출 시스템",
    page_icon="🍱",
    layout="wide"
)

try:
    if not CALL_FILE.exists():
        CALL_FILE.write_text("대기중", encoding="utf-8")
except Exception as e:
    st.error(f"call.txt 생성 오류: {e}")
    st.stop()

if "current_call" not in st.session_state:
    try:
        st.session_state.current_call = CALL_FILE.read_text(encoding="utf-8")
    except Exception as e:
        st.session_state.current_call = "오류 발생"
        st.error(f"call.txt 읽기 오류: {e}")

st.subheader("현재 상태")
st.info(st.session_state.current_call)

st.divider()
st.subheader("반 호출")


def set_call(text: str):
    CALL_FILE.write_text(text, encoding="utf-8")
    st.session_state.current_call = text


def reset_call():
    CALL_FILE.write_text("대기중", encoding="utf-8")
    st.session_state.current_call = "대기중"


# 1학년
st.markdown("### 1학년")
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = st.columns(11)

with col1:
    st.button("1학년 1반", on_click=set_call, args=("1학년 1반 출발!",))

with col2:
    st.button("1학년 2반", on_click=set_call, args=("1학년 2반 출발!",))

with col3:
    st.button("1학년 3반", on_click=set_call, args=("1학년 3반 출발!",))

with col4:
    st.button("1학년 4반", on_click=set_call, args=("1학년 4반 출발!",))

with col5:
    st.button("1학년 5반", on_click=set_call, args=("1학년 5반 출발!",))

with col6:
    st.button("1학년 6반", on_click=set_call, args=("1학년 6반 출발!",))

with col7:
    st.button("1학년 7반", on_click=set_call, args=("1학년 7반 출발!",))

with col8:
    st.button("1학년 8반", on_click=set_call, args=("1학년 8반 출발!",))

with col9:
    st.button("1학년 9반", on_click=set_call, args=("1학년 9반 출발!",))

with col10:
    st.button("1학년 10반", on_click=set_call, args=("1학년 10반 출발!",))

with col11:
    st.button("1학년 전체", on_click=set_call, args=("1학년 전체 출발!",))

st.divider()

# 2학년 (확장 예시)
st.markdown("### 2학년")
col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22 = st.columns(11)

with col12:
    st.button("2학년 1반", on_click=set_call, args=("2학년 1반 출발!",))

with col13:
    st.button("2학년 2반", on_click=set_call, args=("2학년 2반 출발!",))

with col14:
    st.button("2학년 3반", on_click=set_call, args=("2학년 3반 출발!",))

with col15:
    st.button("2학년 4반", on_click=set_call, args=("2학년 4반 출발!",))

with col16:
    st.button("2학년 5반", on_click=set_call, args=("2학년 5반 출발!",))

with col17:
    st.button("2학년 6반", on_click=set_call, args=("2학년 6반 출발!",))

with col18:
    st.button("2학년 7반", on_click=set_call, args=("2학년 7반 출발!",))

with col19:
    st.button("2학년 8반", on_click=set_call, args=("2학년 8반 출발!",))

with col20:
    st.button("2학년 9반", on_click=set_call, args=("2학년 9반 출발!",))

with col21:
    st.button("2학년 10반", on_click=set_call, args=("2학년 10반 출발!",))

with col22:
    st.button("2학년 전체", on_click=set_call, args=("2학년 전체 출발!",))

st.divider()

# 3학년 (확장 예시)
st.markdown("### 3학년")
col23, col24, col25, col26, col27, col28, col29, col30, col31, col32, col33 = st.columns(11)

with col23:
    st.button("3학년 1반", on_click=set_call, args=("3학년 1반 출발!",))

with col24:
    st.button("3학년 2반", on_click=set_call, args=("3학년 2반 출발!",))

with col25:
    st.button("3학년 3반", on_click=set_call, args=("3학년 3반 출발!",))

with col26:
    st.button("3학년 4반", on_click=set_call, args=("3학년 4반 출발!",))

with col27:
    st.button("3학년 5반", on_click=set_call, args=("3학년 5반 출발!",))

with col28:
    st.button("3학년 6반", on_click=set_call, args=("3학년 6반 출발!",))

with col29:
    st.button("3학년 7반", on_click=set_call, args=("3학년 7반 출발!",))

with col30:
    st.button("3학년 8반", on_click=set_call, args=("3학년 8반 출발!",))

with col31:
    st.button("3학년 9반", on_click=set_call, args=("3학년 9반 출발!",))

with col32:
    st.button("3학년 10반", on_click=set_call, args=("3학년 10반 출발!",))

with col33:
    st.button("3학년 전체", on_click=set_call, args=("3학년 전체 출발!",))

st.divider()

st.markdown("### 상태 초기화")
if st.button("초기화", type="secondary"):
    reset_call()
    st.success("상태가 초기화되었습니다.")
