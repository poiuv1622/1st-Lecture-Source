import streamlit as st

st.title("나만의 계산기")
st.write("""
---
**사용 가능한 연산**
1. 덧셈 (+)
2. 뺄셈 (-)
3. 곱셈 (×)
4. 나누기 (÷)
---
""")

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def time(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "오류: 0으로 나눌 수 없습니다."
    return x / y

# 연산 선택
operation = st.selectbox(
    "원하는 연산을 선택해주세요.",
    ("덧셈 (+)", "뺄셈 (-)", "곱셈 (×)", "나누기 (÷)")
)

# 숫자 입력
x = st.number_input("첫 번째 숫자를 입력해주세요.", value=0.0, format="%.5f")
y = st.number_input("두 번째 숫자를 입력해주세요.", value=0.0, format="%.5f")

if st.button("계산하기"):
    if operation == "덧셈 (+)":
        result = plus(x, y)
        st.success(f"결과: {result}")
    elif operation == "뺄셈 (-)":
        result = minus(x, y)
        st.success(f"결과: {result}")
    elif operation == "곱셈 (×)":
        result = time(x, y)
        st.success(f"결과: {result}")
    elif operation == "나누기 (÷)":
        result = divide(x, y)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"결과: {result}")

