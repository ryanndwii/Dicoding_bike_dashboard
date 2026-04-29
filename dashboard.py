import streamlit as st
import pandas as pd
import matplotlib
st.write("Matplotlib version:", matplotlib.__version__)

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide",
    page_icon="🚴"
)

#Load Data
@st.cache_data
def load_data():
    day = pd.read_csv('day_clean.csv')
    hour = pd.read_csv('hour_clean.csv')
    return day, hour

day, hour = load_data()


st.title("🚴 Bike Sharing Dashboard")
st.markdown("Analisis Penyewaan Sepeda berdasarkan Waktu, Cuaca, dan Tipe Pengguna")

#KPI
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", f"{day['cnt'].sum():,.0f}")
col2.metric("Rata-rata Harian", f"{day['cnt'].mean():.0f}")
col3.metric("Rata-rata Per Jam", f"{hour['cnt'].mean():.0f}")

st.divider()

#Filter
st.sidebar.header("🔎 Filter")

selected_year = st.sidebar.selectbox(
    "Pilih Tahun",
    options=[0, 1],
    format_func=lambda x: "2011" if x == 0 else "2012"
)

filtered_hour = hour[hour['yr'] == selected_year]
filtered_day = day[day['yr'] == selected_year]

#Visualisasi 1
col1, col2 = st.columns(2)

# Peak Hour
with col1:
    st.subheader("🕒 Peak Hour Analysis")
    hourly_avg = filtered_hour.groupby('hr')['cnt'].mean()

    fig1, ax1 = plt.subplots()
    hourly_avg.plot(ax=ax1)
    ax1.set_title("Rata-rata Penyewaan per Jam")
    ax1.set_xlabel("Jam")
    ax1.set_ylabel("Jumlah Penyewaan")
    ax1.grid()

    st.pyplot(fig1)
    st.caption("Peak hour: 07–09 & 16–20")

# Weather
with col2:
    st.subheader("🌦️ Pengaruh Cuaca")
    weather_avg = filtered_day.groupby('weathersit')['cnt'].mean()

    fig2, ax2 = plt.subplots()
    weather_avg.plot(kind='bar', ax=ax2)
    ax2.set_title("Penyewaan Berdasarkan Cuaca")
    ax2.set_xlabel("Cuaca (1=Cerah, 2=Berawan, 3=Buruk)")
    ax2.set_ylabel("Jumlah Penyewaan")

    st.pyplot(fig2)
    st.caption("Penurunan signifikan saat cuaca buruk (~63%)")

st.divider()

#Visualisasi 2
col3, col4 = st.columns(2)

# User Segmentation
with col3:
    st.subheader("👥 User Segmentation")
    user_seg = filtered_hour.groupby('hr')[['casual', 'registered']].mean()

    fig3, ax3 = plt.subplots()
    user_seg.plot(ax=ax3)
    ax3.set_title("Casual vs Registered")
    ax3.set_xlabel("Jam")
    ax3.set_ylabel("Jumlah Penyewaan")

    st.pyplot(fig3)
    st.caption("Registered dominan saat jam kerja")

# Workingday vs Holiday
with col4:
    st.subheader("📅 Hari Kerja vs Libur")
    workday = hour.groupby(['workingday','hr'])['cnt'].mean().unstack()

    fig4, ax4 = plt.subplots()
    workday.T.plot(ax=ax4)
    ax4.set_title("Perbandingan Pola Jam")
    ax4.set_xlabel("Jam")
    ax4.set_ylabel("Jumlah Penyewaan")

    st.pyplot(fig4)
    st.caption("Hari kerja: commuting | Libur: rekreasi")

st.divider()
st.caption("🚀 Bike Sharing Dashboard | Data Analysis Project")