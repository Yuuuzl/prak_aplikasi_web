import streamlit as st
import pandas as pd
import altair as alt
from transformers import pipeline  # HuggingFace Transformers

# Memuat model IndoBERT dari HuggingFace
nlp = pipeline("sentiment-analysis", model="w11wo/indonesian-roberta-base-sentiment-classifier")

# Fungsi untuk analisis sentimen menggunakan IndoBERT
def analyze_indonesian_sentiment(text):
    result = nlp(text)
    return result

# Fungsi utama
def main():
    st.title("Sentiment Analysis NLP App")
    st.subheader("Streamlit Projects")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

        # Membuat form input 
        with st.form("nlpForm"):
            raw_text = st.text_area("Enter Text Here")
            submit_button = st.form_submit_button(label='Analyze')

        # Layout
        col1, col2 = st.columns(2)

        if submit_button:
            with col1:
                st.info("Results")

                # Analisis sentimen menggunakan IndoBERT
                sentiment_result = analyze_indonesian_sentiment(raw_text)
                
                # Menampilkan hasil analisis
                st.write("Hasil Sentimen:", sentiment_result)

                # Ambil label dan skor sentimen dari hasil prediksi
                label = sentiment_result[0]['label']
                score = sentiment_result[0]['score']

                # Debugging: Tampilkan isi label yang dikembalikan model
                st.write("Label yang dikembalikan:", label)

                # Emoji berdasarkan hasil IndoBERT
                if label == "positive":
                    st.markdown(f"**Sentiment: Positive 😊 (Confidence: {score:.2f})**")
                elif label == "negative":
                    st.markdown(f"**Sentiment: Negative 😡 (Confidence: {score:.2f})**")
                else:
                    st.markdown(f"**Sentiment: Neutral 😐 (Confidence: {score:.2f})**")

                # Debugging: Tampilkan hasil sentimen mentah
                st.write("Sentiment Result (Raw):", sentiment_result)

                # Konversi hasil ke DataFrame untuk visualisasi
                result_df = pd.DataFrame(sentiment_result)
                st.dataframe(result_df)

                # Visualisasi menggunakan Altair
                c = alt.Chart(result_df).mark_bar().encode(
                    x=alt.X('label', title='Sentiment Label'),
                    y=alt.Y('score', title='Confidence Score'),
                    color='label'
                )
                st.altair_chart(c, use_container_width=True)

            with col2:
                st.info("Token Sentiment")

                # Analisis sentimen per kata/token
                token_sentiments = analyze_token_sentiment(raw_text)
                st.write(token_sentiments)

    else:
        st.subheader("About")

# Fungsi untuk menganalisis sentimen per token
def analyze_token_sentiment(docx):
    tokens = docx.split()
    token_sentiments = []

    # Analisis setiap token menggunakan IndoBERT
    for token in tokens:
        sentiment = analyze_indonesian_sentiment(token)
        token_sentiments.append({token: sentiment[0]['label']})
    
    return token_sentiments

# Memanggil fungsi utama
if __name__ == '__main__':
    main()