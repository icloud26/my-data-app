import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="서울 연평균 기온 변화",
    page_icon="🌡️",
    layout="wide"
)

# 제목
st.title("🌡️ 서울의 연평균 기온 변화")
st.write("1907년 이후 서울의 연평균 기온이 어떻게 변해 왔는지 살펴봅니다.")

# 데이터 주소
url = "https://raw.githubusercontent.com/greatsong/modudata/main/data/seoul.csv"


# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv(url)

    # 날짜를 날짜 형식으로 변환
    df["날짜"] = pd.to_datetime(df["날짜"])

    # 연도 열 만들기
    df["연도"] = df["날짜"].dt.year

    return df


df = load_data()


# 연도별 평균기온 계산
yearly_temp = (
    df.groupby("연도")["평균기온"]
    .mean()
    .reset_index()
)

# 선 그래프
st.subheader("연도별 평균기온")

chart_data = yearly_temp.set_index("연도")

st.line_chart(
    chart_data,
    y="평균기온",
    x_label="연도",
    y_label="평균기온 (℃)"
)

# 안내
st.info(
    "※ 1907년의 데이터는 10월 1일부터 시작하므로 "
    "1907년 평균은 1년 전체의 평균기온이 아닙니다."
)

# 데이터 확인
with st.expander("연도별 평균기온 데이터 보기"):
    st.dataframe(
        yearly_temp,
        use_container_width=True,
        hide_index=True
    )
