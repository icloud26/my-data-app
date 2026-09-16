import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(
    page_title="서울 일별 평균기온 분포",
    page_icon="🌡️",
    layout="wide"
)

# 제목
st.title("🌡️ 서울의 일별 평균기온 분포")
st.write(
    "1907년 이후 서울의 일별 평균기온이 "
    "어느 온도 구간에 많이 분포하는지 살펴봅니다."
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

# 결측값 제거
temperature = df["평균기온"].dropna()

# 히스토그램
st.subheader("일별 평균기온 히스토그램")

fig, ax = plt.subplots(figsize=(10, 5))

ax.hist(
    temperature,
    bins=30,
    edgecolor="black"
)

ax.set_xlabel("Average Temperature (°C)")
ax.set_ylabel("Number of Days")
ax.set_title("Distribution of Daily Average Temperature in Seoul")
ax.grid(axis="y", alpha=0.3)

st.pyplot(fig)

# 간단한 통계 정보
st.subheader("평균기온 통계")

st.write(f"전체 관측 일수: {len(temperature):,}일")
st.write(f"평균기온: {temperature.mean():.1f}℃")
st.write(f"가장 낮은 일평균기온: {temperature.min():.1f}℃")
st.write(f"가장 높은 일평균기온: {temperature.max():.1f}℃")
