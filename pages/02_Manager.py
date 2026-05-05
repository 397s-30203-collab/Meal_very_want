import streamlit as st
from pathlib import Path
import tempfile
from datetime import datetime
from openpyxl import Workbook, load_workbook

st.set_page_config(
    page_title="🚦 청주여고 급식실 정거장",
    page_icon="https://i.postimg.cc/Fs7hFRWN/seukeulinsyas-2026-01-14-065826.png",
    layout="wide"
)

st.title("관리자 페이지")

# ---------------- 로그인 기능 ----------------
PASSWORD = "cat123!"

if "login_ok" not in st.session_state:
    st.session_state.login_ok = False

def login():
    if st.session_state.password_input == PASSWORD:
        st.session_state.login_ok = True
        st.rerun()
    else:
        st.error("비밀번호가 틀렸습니다")

if not st.session_state.login_ok:
    st.subheader("🔐 관리자 인증 필요")
    st.text_input("비밀번호", type="password", key="password_input")
    st.button("로그인", on_click=login)
    st.stop()
# -------------------------------------------

CALL_FILE = Path(tempfile.gettempdir()) / "call.txt"
EXCEL_FILE = Path(tempfile.gettempdir()) / "call_log.xlsx"

# 엑셀 초기 생성
def init_excel():
    if not EXCEL_FILE.exists():
        wb = Workbook()
        ws = wb.active
        ws.title = "로그"
        ws.append(["날짜", "시간", "호출반"])
        wb.save(EXCEL_FILE)

# 호출 기록 저장
def save_call_log(class_name):
    init_excel()
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.append([date, time, class_name])
    wb.save(EXCEL_FILE)

try:
    if not CALL_FILE.exists():
        CALL_FILE.write_text("대기중", encoding="utf-8")
except Exception as e:
    st.error(f"call.txt 생성 오류: {e}")
    st.stop()

if "current_call" not in st.session_state:
    try:
        st.session_state.current_call = CALL_FILE.read_text(encoding="utf-8")
    except:
        st.session_state.current_call = "오류 발생"

st.subheader("현재 상태")
st.info(st.session_state.current_call)

st.divider()
st.subheader("반 호출")

def set_call(text: str):
    CALL_FILE.write_text(text, encoding="utf-8")
    st.session_state.current_call = text
    save_call_log(text)   # ⭐ 엑셀 저장

def reset_call():
    CALL_FILE.write_text("대기중", encoding="utf-8")
    st.session_state.current_call = "대기중"

# 1학년
st.markdown("### 1학년")
cols = st.columns(11)
for i in range(10):
    cols[i].button(f"1학년 {i+1}반", on_click=set_call, args=(f"1학년 {i+1}반 출발!",))
cols[10].button("1학년 전체", on_click=set_call, args=("1학년 전체 출발!",))

st.divider()

# 2학년
st.markdown("### 2학년")
cols = st.columns(11)
for i in range(10):
    cols[i].button(f"2학년 {i+1}반", on_click=set_call, args=(f"2학년 {i+1}반 출발!",))
cols[10].button("2학년 전체", on_click=set_call, args=("2학년 전체 출발!",))

st.divider()

# 3학년
st.markdown("### 3학년")
cols = st.columns(11)
for i in range(10):
    cols[i].button(f"3학년 {i+1}반", on_click=set_call, args=(f"3학년 {i+1}반 출발!",))
cols[10].button("3학년 전체", on_click=set_call, args=("3학년 전체 출발!",))

st.divider()

st.markdown("### 상태 초기화")
if st.button("초기화"):
    reset_call()
    st.success("상태가 초기화되었습니다.")

# 로그아웃
if st.button("로그아웃"):
    st.session_state.login_ok = False
    st.rerun()

# ⭐⭐⭐ 엑셀 다운로드 추가 ⭐⭐⭐
st.divider()
st.subheader("📊 호출 로그 다운로드")

if EXCEL_FILE.exists():
    with open(EXCEL_FILE, "rb") as f:
        st.download_button(
            label="엑셀 다운로드",
            data=f,
            file_name="급식호출로그.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.info("아직 호출 기록이 없습니다.")
