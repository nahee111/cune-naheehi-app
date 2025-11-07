import streamlit as st

 # ...existing code...
import streamlit as st
import random

st.title("🎮 가위바위보 게임")
st.write("나와 가위바위보를 해요 — 버튼을 눌러 선택하세요. 승패는 기록됩니다.")

# 세션 상태 초기화
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0
if "last_round" not in st.session_state:
    st.session_state.last_round = None

choices = ["가위", "바위", "보"]
emoji = {"가위": "✌️", "바위": "✊", "보": "🖐️"}

st.subheader("점수")
st.write(f"나: {st.session_state.user_score}  —  컴퓨터: {st.session_state.comp_score}")

st.markdown("---")
st.subheader("선택")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button(f"가위 {emoji['가위']}"):
        user_choice = "가위"
        st.session_state.last_round = user_choice
with col2:
    if st.button(f"바위 {emoji['바위']}"):
        user_choice = "바위"
        st.session_state.last_round = user_choice
with col3:
    if st.button(f"보 {emoji['보']}"):
        user_choice = "보"
        st.session_state.last_round = user_choice

# 게임 실행 (버튼이 눌렸을 때)
if st.session_state.last_round is not None:
    user = st.session_state.last_round
    comp = random.choice(choices)
    st.write(f"당신: {user} {emoji[user]}  vs  컴퓨터: {comp} {emoji[comp]}")

    # 가위바위보 규칙
    wins = {"가위": "보", "바위": "가위", "보": "바위"}

    if user == comp:
        st.info("비겼습니다.")
    elif wins[user] == comp:
        st.success("이겼습니다! 🎉")
        st.session_state.user_score += 1
    else:
        st.error("졌습니다. 😢")
        st.session_state.comp_score += 1

    # 라운드 초기화(같은 선택으로 연속 누름 방지)
    st.session_state.last_round = None

st.markdown("---")
if st.button("초기화"):
    st.session_state.user_score = 0
    st.session_state.comp_score = 0
    st.success("점수가 초기화되었습니다.")
# ...existing code...