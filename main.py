import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(
    page_title="서울 최저기온과 최고기온의 관계",
    page_icon="🌡️",
    layout="wide"
)

# 제목
st.title("🌡️ 서울의 최저기온과 최고기온의 관계")
st.write(
    "1907년 이후 서울의 날마다의 최저기온과 최고기온이 "
    "어떤 관계를 보이는지 산점도로 살펴봅니다."
)

# 데이터 주소
url = "https://raw.githubusercontent.com/greatsong/modudata/main/data/seoul.csv"


# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv(url)
    df["날짜"] = pd.to_datetime(df["날짜"])
    return df


df = load_data()

# 최저기온과 최고기온에 결측값이 있는 행 제거
temp = df[["최저기온", "최고기온"]].dropna()

# 산점도
st.subheader("일별 최저기온과 최고기온 산점도")

fig, ax = plt.subplots(figsize=(9, 7))

ax.scatter(
    temp["최저기온"],
    temp["최고기온"],
    alpha=0.3,
    s=10
)

ax.set_xlabel("Minimum Temperature (°C)")
ax.set_ylabel("Maximum Temperature (°C)")
ax.set_title("Daily Minimum vs Maximum Temperature in Seoul")
ax.grid(alpha=0.3)

st.pyplot(fig)

# 상관계수 계산
correlation = temp["최저기온"].corr(temp["최고기온"])

st.subheader("두 기온의 관계")
st.write(f"최저기온과 최고기온의 상관계수: **{correlation:.2f}**")

st.info(
    "점들이 오른쪽 위 방향으로 모여 있다면, "
    "최저기온이 높은 날에는 최고기온도 대체로 높다는 뜻입니다."
)
