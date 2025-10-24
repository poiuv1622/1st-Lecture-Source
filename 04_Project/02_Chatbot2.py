import streamlit as st
import copy  # 깊은 복사용
from openai import AzureOpenAI

# 1. OpenAI 및 설정정보
endpoint ="https://internal-apigw-kr.hmg-corp.io/hchat-in/api/v2/01K6ET0Y7FMK2PN72HDMZ4P9W6"
api_key = "OYlOck5vnTLYUF7iE2hmeZlK2Z84bR0gLsSwC5em4zyDIpBSvzQXChRDaBopvWw"

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-21"
)

# 2. 세션 상태: 대화 히스토리 및 이메일 모드
if "history" not in st.session_state:
    st.session_state["history"] = [
        {"role": "assistant", "content": "안녕하세요! 궁금한 점을 입력해주세요."}
    ]
if "email_mode" not in st.session_state:
    st.session_state["email_mode"] = False

# 이메일모드 토글 버튼
email_btn = (
    "📧 이메일 모드: ON (클릭해서 끄기)" if st.session_state["email_mode"]
    else "✉️ 이메일 모드: OFF (클릭해서 켜기)"
)
if st.button(email_btn):
    st.session_state["email_mode"] = not st.session_state["email_mode"]
    st.experimental_rerun()  # 토글 시 버튼 중복방지

# 대화 출력 함수
def display_chat():
    for msg in st.session_state["history"]:
        role = "user" if msg["role"] == "user" else "assistant"
        st.chat_message(role).markdown(msg["content"])

# 사용자 입력 받기
user_input = st.chat_input("메시지를 입력하세요.")

if user_input:
    st.session_state["history"].append({"role": "user", "content": user_input})

    # 시스템 메시지 삽입 (이메일 모드일 때만)
    messages = copy.deepcopy(st.session_state["history"])
    if st.session_state["email_mode"]:
        email_system_message = {
            "role": "system", 
            "content": (
                '''
                너는 전문적인 업무용 이메일 초안 작성 도우미야.
사용자가 제공한 주요 정보와 상황에 맞게, 명확하고 간결하며 정중한 비즈니스 이메일의 초안을 작성해줘.
아래의 지침을 반드시 준수해.

1. 구조 및 형식

인사말부터 시작하고, 적절한 맺음말로 종료할 것
필요한 경우 제목(Subject)을 제안할 것
각 문단은 핵심 메시지가 명확히 드러나도록 구성할 것
2. 문체와 톤

예의 바르고, 전문적이고, 간결한 언어를 사용할 것
부적절하거나 구어체 표현, 이모티콘, 지나치게 친근한 말투 지양
필요에 따라 존댓말, 격식을 갖춘 문장을 사용할 것
3. 맞춤화

사용자가 입력한 목적, 수신자 정보, 상황에 따라 내용과 표현을 맞춤 조정할 것
명확하지 않은 정보는 자연스럽게 보완하여 작성할 것
4. 예시 출력 형태
사용자 입력 예시:

목적: 일정 조율
수신자: 거래처 담당자 김성진 과장
주요 내용: 이번 주 중 미팅 가능 날짜 문의
출력 예시:
Subject: 이번 주 미팅 일정 문의드립니다

안녕하세요, 김성진 과장님.

귀하와의 미팅 일정을 조율하기 위해 연락드립니다. 혹시 이번 주 중 가능한 날짜를 알려주실 수 있을지요?
저희 쪽은 수요일과 금요일 오후 시간대가 가능합니다. 과장님께서 편하신 일정이 있으시면 알려주시면 감사하겠습니다.

답변 기다리겠습니다.
감사합니다.

홍길동 드림
5. 기타

필요 시, 감사 인사/추가 요청/문의 등 사용자 요구사항을 반영할 것
불필요한 반복이나 장황한 표현 지양
명확한 액션(예: 답변 요청, 확인 요청 등) 포함
                '''
             )
        }
        # system 메시지는 always 맨 앞에만 있도록 보정
        if messages and messages[0].get("role") == "system":
            messages[0] = email_system_message
        else:
            messages = [email_system_message] + messages

    # LLM 호출
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=messages
        )
        bot_message = response.choices[0].message.content if response and response.choices else "⚠️ 응답이 없습니다."
    except Exception as e:
        bot_message = f"⚠️ 오류가 발생했습니다: {str(e)}"

    st.session_state["history"].append({"role": "assistant", "content": bot_message})

# 대화 내역을 한 번만 호출(최신 상태 반영)
display_chat()
