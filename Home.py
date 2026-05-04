import streamlit as st

st.set_page_config(
    page_title="🚦 청주여고 급식실 정거장",
    page_icon="https://i.postimg.cc/Fs7hFRWN/seukeulinsyas-2026-01-14-065826.png",
    layout="wide"
)

st.title("🚦 청주여고 급식실 정거장 https://i.postimg.cc/Fs7hFRWN/seukeulinsyas-2026-01-14-065826.png")

st.markdown("""
## 시스템 안내

이 시스템은 학교 급식 시간에 각 반의 호출 상황을 관리하고, 급식 메뉴를 확인할 수 있도록 합니다.

### 📱 기능

- **👩‍🏫 Student**: 오늘의 학교 급식 메뉴와 현재 호출 반 확인
- **👩‍🍳 Manager**: 각 반을 호출하고 상태를 관리
""")

st.info("💡 좌측 사이드바의 메뉴를 선택하여 시작하세요!")
