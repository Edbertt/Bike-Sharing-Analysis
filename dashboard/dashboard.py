# Mengimport library yang akan digunakan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membuat function untuk membantu mengelompokan data
def create_season_order_df(hour_df):
    seasons_orders_df = hour_df.groupby(["season","yr"]).agg({
        "casual" : "sum",
        "registered" : "sum",
        "cnt" : "sum"
    })
    return seasons_orders_df

def create_hour_order_df(hour_df):
    hours_orders_df = hour_df.groupby(["hr","yr"]).agg({
        "casual" : "sum",
        "registered" : "sum",
        "cnt" : "sum"
    })
    return hours_orders_df

# Membuka file csv yang sudah dicleaning
hour_df = pd.read_csv("../dashboard/cleaned_hour.csv")
st.set_page_config(page_title="Bike-Sharing Dashboard",layout="wide") # Menetapkan judul halaman

# Komponen sidebar
st.sidebar.header("Description : ")
st.sidebar.markdown("This is Dashboard for summarize data on Bike-Sharing Dataset")

# Membuat pengelompokan data dari function yang telah dibuat
season_order_df = create_season_order_df(hour_df)
hour_order_df = create_hour_order_df(hour_df)

# Komponen main body
st.title(":bar_chart: Bike-Sharing Dashboard")
st.markdown("##")

# Menampilkan jumlah total dari casual, registered, dan keduannya dari tahun 2011-2012
col1, col2, col3 = st.columns(3)

with col1:
    total_all_rides = hour_df['cnt'].sum()
    st.metric("Total Rides", value=total_all_rides)
with col2:
    total_casual_rides = hour_df['casual'].sum()
    st.metric("Total Casual Rides", value=total_casual_rides)
with col3:
    total_registered_rides = hour_df['registered'].sum()
    st.metric("Total Registered Rides", value=total_registered_rides)

st.markdown("---")

# Menampilkan hasil visualisasi yang telah dibuat
fig, ax = plt.subplots(figsize=(16,10))

st.markdown("Bar Chart untuk jumlah rental berdasarkan musim:")

sns.barplot(data=season_order_df,x="season",y="cnt", hue="yr", ax=ax)
ax.set_title("Perbadingan jumlah rental antara 2011 dan 2012 berdasarkan musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Total Rental")
st.pyplot(fig)

st.markdown("Bar Chart untuk jumlah rental berdasarkan jam:")

fig, ax = plt.subplots(figsize=(16,10))
sns.barplot(data=hour_order_df,x="hr",y="cnt", hue="yr",width = 0.7, ax=ax)
ax.set_title("Perbandingan jumlah rental per jam antara tahun 2011 dan 2012")
ax.set_xlabel("Jam ke-")
ax.set_ylabel("Jumlah Rental")

st.pyplot(fig)

st.caption('Copyright (c), created by Edbert')
