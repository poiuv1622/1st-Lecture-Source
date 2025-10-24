# 필요한 라이브러리 임포트
import streamlit as st                     # Streamlit 웹 앱 라이브러리
from openai import AzureOpenAI             # Azure 기반 OpenAI 클라이언트

# 환경변수 또는 직접 입력으로 설정값 가져오기
# 반드시 본인 정보로 채워주세요!
endpoint ="https://internal-apigw-kr.hmg-corp.io/hchat-in/api/v2/01K6ET0Y7FMK2PN72HDMZ4P9W6"
api_key = "OYlOck5vnTLYUF7iE2hmeZlK2Z84bR0gLsSwC5em4zyDIpBSvzQXChRDaBopvWw"

# AzureOpenAI 클라이언트 초기화
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-21"
)

# Streamlit 앱 제목
st.title("💬 LLM 챗봇 데모")

# 대화 기록 세션 state 초기화 및 관리
if "history" not in st.session_state:
    st.session_state["history"] = [
        {"role": "assistant", "content": "안녕하세요! 궁금한 점을 입력해주세요."}
    ]

# 대화 기록 출력 함수
def display_chat():
    """세션의 대화 히스토리를 Streamlit 채팅 UI로 표시."""
    for msg in st.session_state["history"]:
        if msg["role"] == "user":
            st.chat_message("user").markdown(msg["content"])
        else:
            st.chat_message("assistant").markdown(msg["content"])

# 챗 기록 표시
display_chat()

# 입력창 (Streamlit 1.29 이후 st.chat_input 사용 가능)
user_input = st.chat_input(
    "메시지를 입력하세요."
)

# 사용자가 메시지를 입력한 경우:
if user_input:
    # 대화 기록에 사용자 입력 추가
    st.session_state["history"].append({"role": "user", "content": user_input})
    display_chat()

    # LLM OpenAI API로 이전 대화 전체 전달 및 답변 생성
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",                 # 원하는 모델명
            messages=st.session_state["history"]  # 전체 대화 내역
        )
        bot_message = response.choices[0].message.content
    except Exception as e:
        bot_message = f"⚠️ 오류가 발생했습니다: {str(e)}"

    # 대화 기록에 Assistant 답변 추가
    st.session_state["history"].append(
        {"role": "assistant", "content": bot_message}
    )

    # 최신까지 채팅 기록 다시 표시
    display_chat()
