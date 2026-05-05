import streamlit as st
from pathlib import Path
import tempfile
from openpyxl import Workbook, load_workbook
from datetime import datetime
from zoneinfo import ZoneInfo   # ⭐ 한국시간용 추가

st.set_page_config(page_title="관리자", layout="wide")
st.title("👩‍🏫 급식 호출 관리자 페이지")

# ==============================
# 🔐 로그인
# ==============================
ADMIN_PASSWORD = "cat123!"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.subheader("관리자 로그인")
    pw = st.text_input("비밀번호", type="password")

    if st.button("로그인"):
        if pw == ADMIN_PASSWORD:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("비밀번호 틀림")
    st.stop()

# ==============================
# 📁 파일 준비
# ==============================
BASE_DIR = Path(tempfile.gettempdir())
CALL_FILE = BASE_DIR / "call.txt"
EXCEL_FILE = BASE_DIR / "data.xlsx"

if not CALL_FILE.exists():
    CALL_FILE.write_text("대기중", encoding="utf-8")

if not EXCEL_FILE.exists():
    wb = Workbook()
    ws = wb.active
    ws.append(["기록", "날짜", "시간"])
    wb.save(EXCEL_FILE)

# ==============================
# ⏰ 엑셀 기록 (한국시간 적용)
# ==============================
def save_log(action):
    now = datetime.now(ZoneInfo("Asia/Seoul"))  # ⭐ 한국시간 고정
    date_str = now.strftime("%Y-%m-%d")         # ⭐ 날짜 . 형식
    time_str = now.strftime("%H:%M:%S")         # ⭐ 시간 : 형식

    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.append([action, date_str, time_str])
    wb.save(EXCEL_FILE)

# ==============================
# 📢 호출 함수
# ==============================
def set_call(message):
    CALL_FILE.write_text(message, encoding="utf-8")
    save_log(message)  # ⭐ 버튼 누를 때마다 기록됨
    st.rerun()

def reset_call():
    CALL_FILE.write_text("대기중", encoding="utf-8")
    save_log("호출 초기화")
    st.rerun()

# ==============================
# 📢 현재 상태 표시
# ==============================
st.subheader("현재 호출 상태")
current_call = CALL_FILE.read_text(encoding="utf-8")
st.info(current_call)

st.divider()

# ==============================
# ⭐ 1학년 호출
# ==============================
st.markdown("### 🎒 1학년")
cols = st.columns(11)
for i in range(10):
    cols[i].button(f"1학년 {i+1}반", on_click=set_call, args=(f"1학년 {i+1}반 출발!",))
cols[10].button("1학년 전체", on_click=set_call, args=("1학년 전체 출발!",))

st.divider()

# ==============================
# ⭐ 2학년 호출
# ==============================
st.markdown("### 🎒 2학년")
cols = st.columns(11)
for i in range(10):
    cols[i].button(f"2학년 {i+1}반", on_click=set_call, args=(f"2학년 {i+1}반 출발!",))
cols[10].button("2학년 전체", on_click=set_call, args=("2학년 전체 출발!",))

st.divider()

# ==============================
# ⭐ 3학년 호출
# ==============================
st.markdown("### 🎒 3학년")
cols = st.columns(11)
for i in range(10):
    cols[i].button(f"3학년 {i+1}반", on_click=set_call, args=(f"3학년 {i+1}반 출발!",))
cols[10].button("3학년 전체", on_click=set_call, args=("3학년 전체 출발!",))

st.divider()

# ==============================
# 🔄 상태 초기화
# ==============================
st.markdown("### 🔄 상태 초기화")
if st.button("초기화"):
    reset_call()
    st.success("상태가 초기화되었습니다.")

# ==============================
# 📊 엑셀 관리
# ==============================
st.divider()
st.subheader("엑셀 관리")

def reset_excel():
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.delete_rows(2, ws.max_row)  # 헤더 제외 전체 삭제
    wb.save(EXCEL_FILE)

col1, col2 = st.columns(2)

with col1:
    if st.button("🗑 엑셀 초기화"):
        reset_excel()
        st.success("엑셀 데이터 삭제 완료")

with col2:
    with open(EXCEL_FILE, "rb") as f:
        st.download_button(
            label="📥 엑셀 다운로드",
            data=f,
            file_name="급식데이터.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# ==============================
# 🚪 로그아웃
# ==============================
st.divider()
if st.button("로그아웃"):
    st.session_state.login = False
    st.rerun()
