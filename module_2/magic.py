import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'jumlah': [1, 2, 3, 4],
    'harga': [10, 20, 30, 40]
})

st.write(df)

#TEST
#Membuta dataframe sederhana untuk stok barang di minimarket

df = pd.DataFrame({
    'Nama_barang': ['Telur', 'Ayam', 'Beras', 'Gula'],
    'Stok (kg)': [100, 20, 50, 40],
    'Harga/kg (Rp)': [26000, 30000, 12000, 15000]
})

st.write(df)    