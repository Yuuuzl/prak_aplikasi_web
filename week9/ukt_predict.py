# Nama : Wahyu Nur Cahyanto
# NIM  : 22537141026

# Core Pkgs
import streamlit as st
import sklearn
import joblib, os
import numpy as np 

# Load Model
def load_prediction_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

def main():
    """Prediksi UKT Mahasiswa Berdasarkan Pendapatan Orang Tua"""
    
    # Customizing background color and fonts
    page_bg_img = '''
    <style>
    body {
    background-color: #f0f2f6;
    font-family: 'Arial', sans-serif;
    }
    .reportview-container {
        background: white;
        border-radius: 10px;
        padding: 20px;
    }
    .sidebar .sidebar-content {
        background: #20232a;
    }
    h3 {
        color: #ffffff;
        text-align: center;
    }
    h4 {
        font-size: 18px;
        color: #ffffff;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


    html_templ = """
    <div style="background-color:#4b8bbe;padding:10px;border-radius:10px;">
    <h3>Prediksi UKT Mahasiswa</h3>
    </div>
    """
    st.markdown(html_templ, unsafe_allow_html=True)

    activity = ["Prediksi UKT", "Apa itu Regresi?"]
    choice = st.sidebar.selectbox("Menu", activity)

    # UKT Prediction CHOICE
    if choice == 'Prediksi UKT':
        st.markdown("<h4>Berdasarkan Pendapatan Orang Tua</h4>", unsafe_allow_html=True)

        income = st.number_input("Masukkan pendapatan orang tua (dalam Rupiah)", min_value=0)

        if st.button("Prediksi"):
            
            if income <= 500000:
                st.warning("Selamat anda mendapatkan KIP")
                return
            
            regressor = load_prediction_model("linear_regression_ukt.pkl")
            income_reshaped = np.array(income).reshape(-1, 1)

            predicted_ukt = regressor.predict(income_reshaped)

            # Result in a card with more contrast for predicted value
            st.markdown(f"""
                <div style="background-color:#20232a;padding:20px;border-radius:10px;margin-top:20px;">
                <h3>Prediksi UKT</h3>
                <p>Untuk pendapatan orang tua sebesar: <b>Rp {income:,}</b></p>
                
                <h2 style="color:#d9534f; margin: 0;">UKT yang diprediksi adalah:</h2>
                <h2 style="color:#d9534f; margin:0"><b>Rp {predicted_ukt[0][0].round(2):,}</b></h2>
                
            """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
