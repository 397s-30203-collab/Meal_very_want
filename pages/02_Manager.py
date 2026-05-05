import streamlit as st
from pathlib import Path
import tempfile
from openpyxl import Workbook, load_workbook
from datetime import datetime

st.title("👩‍🏫 급식 호출 관리자 페이지")

# ==============================
# 1️⃣ 관리자 로그인
# ==============================
ADMIN_PASSWORD = "1234"

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.subheader("🔐 관리자 로그인")
    pw = st.text_input("비밀번호", type="password")

    if st.button("로그인"):
        if pw == ADMIN_PASSWORD:
            st.session_state.login = True
            st.success("로그인 성공!")
            st.rerun()
        else:
            st.error("비밀번호 틀림")

    st.stop()

# ==============================
# 2️⃣ 파일 경로 준비
# ==============================
BASE_DIR = Path(tempfile.gettempdir())
CALL_FILE = BASE_DIR / "call.txt"
EXCEL_FILE = BASE_DIR / "data.xlsx"

if not CALL_FILE.exists():
    CALL_FILE.write_text("대기중", encoding="utf-8")

# 엑셀 없으면 생성
if not EXCEL_FILE.exists():
    wb = Workbook()
    ws = wb.active
    ws.append(["기록", "날짜", "시간"])
    wb.save(EXCEL_FILE)

# ==============================
# ⭐ 엑셀 기록 함수 (핵심 추가!)
# ==============================
def save_log(action):
    now = datetime.now()
    date_str = now.strftime("%Y.%m.%d")   # 날짜 . 구분
    time_str = now.strftime("%H:%M:%S")   # 시간 : 구분

    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.append([action, date_str, time_str])
    wb.save(EXCEL_FILE)

# ==============================
# 3️⃣ 호출 상태
# ==============================
st.subheader("📢 현재 호출 상태")
current_call = CALL_FILE.read_text(encoding="utf-8")
st.info(f"현재 상태 : {current_call}")

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

# ==============================
# 4️⃣ 엑셀 관리
# ==============================
st.divider()
st.subheader("📊 엑셀 데이터 관리")

def reset_excel():
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.delete_rows(2, ws.max_row)
    wb.save(EXCEL_FILE)

col3, col4 = st.columns(2)

with col3:
    if st.button("🗑 엑셀 초기화"):
        reset_excel()
        st.success("엑셀 데이터 삭제 완료!")

with col4:
    with open(EXCEL_FILE, "rb") as f:
        st.download_button(
            label="📥 엑셀 다운로드",
            data=f,
            file_name="급식데이터.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# ==============================
# 5️⃣ 로그아웃
# ==============================
st.divider()
if st.button("로그아웃"):
    st.session_state.login = False
    st.rerun()
