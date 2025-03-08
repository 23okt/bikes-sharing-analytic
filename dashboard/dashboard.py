import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set_theme(style='dark')

all_df = pd.read_csv("dashboard/all_data.csv")
bikes_per_day_df = pd.read_csv("data/day.csv")
bikes_per_hour_df = pd.read_csv("data/hour.csv")



datetime_columns = ["dteday"]

for column in datetime_columns:
  bikes_per_day_df[column] = pd.to_datetime(bikes_per_day_df[column])
  
for column in datetime_columns:
  bikes_per_hour_df[column] = pd.to_datetime(bikes_per_hour_df[column])


def create_monthly_order_df():
    bikes_per_day_df['year_month'] = bikes_per_day_df['dteday'].dt.to_period('M')
    monthly_trend = bikes_per_day_df.groupby('year_month')['cnt'].sum()
    
    return monthly_trend
    
def total_bikes_per_day():
    bikes_per_day = bikes_per_day_df.groupby(by='weekday').agg({
    "casual": ["sum"],
    "registered": ["sum"],
    "cnt": ["sum"]
})
    return bikes_per_day

def create_bikes_per_season():
    seasonal_usage = bikes_per_hour_df.groupby("season")[["casual", "registered"]].sum()
    seasonal_usage["total"] = seasonal_usage["casual"] + seasonal_usage["registered"]
    seasonal_usage = seasonal_usage.sort_values(by="total", ascending=False)
    
    return seasonal_usage

wind_avg = all_df.groupby('windspeed_y', as_index=False)['cnt_y'].sum()
cnt_min = wind_avg.sort_values(by="cnt_y", ascending=True)
cnt_max = wind_avg.sort_values(by="cnt_y", ascending=False)

with st.sidebar:
    st.header("Bike Sharing Dataset")
    st.image("https://img.freepik.com/premium-vector/young-man-rides-bicycle-flat-style-vector-illustration_787461-1042.jpg",width=100)
    st.subheader("Overview")
    st.write("Dashboard ini dikembangkan untuk menganalisis tren peminjaman sepeda berdasarkan berbagai faktor seperti cuaca, musim, dan kecepatan angin. Visualisasi data membantu dalam memahami pola penggunaan sepeda sepanjang waktu.")
    
monthly_order_df = create_monthly_order_df()
total_bikes_day_df = total_bikes_per_day()
bikes_per_season = create_bikes_per_season()


st.header('Bike Sharing Dashboard 🚲🚀')

col1, col2, col3 = st.columns(3)

with col1:
    total_casual = bikes_per_day_df.casual.sum()
    st.metric("Total Pengguna Reguler", value=total_casual)
    
with col2:
    total_registered = bikes_per_day_df.registered.sum()
    st.metric("Total Pengguna Membership", value=total_registered)
    
with col3:
    total_rentals = all_df.cnt_y.sum()
    st.metric("Total Rental", value=total_rentals)

st.subheader("Tren Peminjaman Sepedar Per Bulan")
monthly_order_df.index = monthly_order_df.index.to_timestamp()

plt.figure(figsize=(12, 8))
sns.lineplot(x=monthly_order_df.index, y=monthly_order_df.values, marker="o", linewidth=2, color="royalblue")
plt.title("Tren Jumlah Peminjaman Sepeda per Bulan", fontsize=14)
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Jumlah Peminjaman Sepeda", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.6)
st.pyplot(plt)

st.markdown("💡 Berdasarkan data visualisasi diatas dapat dilihat bahwa tren peminjaman selalu meningkat pada pertengahan bulan menuju pada akhir bulan.")

st.subheader("Peminjaman Sepeda berdasarkan Weekday")
day_labels = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3"]
sns.barplot(
    x="weekday",
    y="cnt",
    data=bikes_per_day_df.sort_values(by="cnt", ascending=True),
    palette=colors,
    ax=ax
)
ax.set_title("Total Peminjaman Sepeda per Hari", loc="center", fontsize=30)
ax.set_ylabel("Jumlah Peminjaman Sepeda", fontsize=20)
ax.set_xlabel("Hari", fontsize=20)
ax.tick_params(axis='y', labelsize=15)
ax.tick_params(axis='x', labelsize=15)
ax.set_xticks(range(7))
ax.set_xticklabels(day_labels)
st.pyplot(fig)

st.markdown("💡 Berdasarkan data visualisasi terlihat pengguna lebih sering melakukan peminjaman sepeda pada hari menuju akhir pekan seperti kamis, jumat dan sabtu")

st.subheader("Penggunaan Sepeda berdasarkan Musim")
bikes_per_season.index = ['Fall', 'Summer', 'Winter', 'Springer']
bikes_per_season[['casual', 'registered']].plot(kind='bar', figsize=(10, 6))

plt.title('Penggunaan Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Pengguna')
plt.xticks(rotation=0)
st.pyplot(plt)

st.markdown("💡 Berdasarkan data visualisasi pengguna casual cenderung lebih sering melakukan peminjaman pada musim Fall dan Summer")
st.markdown("💡 Berdasarkan data visualisasi pengguna registered cenderung lebih stabil dalam melakukan peminjaman sepeda")

st.subheader("Pengaruh Kecepatan Angin pada Peminjaman Sepeda")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35,15))

colors_max = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3"]
colors_min = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#90CAF9"]

sns.barplot(x="windspeed_y", y="cnt_y", data=cnt_max.head(5), palette=colors_max, ax=ax[0])
ax[0].set_ylabel("Jumlah Peminjaman Sepeda", fontsize=30)
ax[0].set_xlabel("Kecepatan Angin", fontsize=30)
ax[0].set_title("Peminjaman Sepeda Tertinggi", loc="center", fontsize=50)
ax[0].tick_params(axis="y", labelsize=35)
ax[0].tick_params(axis="x", labelsize=30)

sns.barplot(x="windspeed_y", y="cnt_y", data=cnt_min.head(5), palette=colors_min, ax=ax[1])
ax[1].set_ylabel("Jumlah Peminjaman Sepeda", fontsize=30)
ax[1].set_xlabel("Kecepatan Angin", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Peminjaman Sepeda Terendah", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)
st.pyplot(fig)

st.markdown("💡 Pada tabel visualisasi Terendah bisa dilihat bahwa peminjaman sepeda lebih cenderung sedikit ketika kecepatan angin sangat besar karena ini pun berbahaya untuk berkendara sepeda")