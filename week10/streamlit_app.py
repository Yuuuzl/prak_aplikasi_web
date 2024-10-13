import streamlit as st
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Function to clean text
def clean_text(text):
    if isinstance(text, str):
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
        return text
    return ''

# Load the Twitter data
file_path = 'Twitter_Data.csv'  # Update with the correct path if necessary
df = pd.read_csv(file_path)

# Clean the text data
df['cleaned_text'] = df['clean_text'].apply(clean_text)

# Set up the Streamlit app
st.title("Twitter Data NLP Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.selectbox(
    "Choose a section:",
    ["Cleaned Data", "Word Cloud", "Sentiment Analysis", "Top Words", "Most Recent Tweet"]
)


# Section: Cleaned Data
if options == "Cleaned Data":
    st.subheader("Cleaned Tweets")
    st.dataframe(df[['cleaned_text', 'category']])

# Section: Word Cloud
if options == "Word Cloud":
    st.subheader("Word Cloud")
    all_text = ' '.join(df['cleaned_text'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Hide axis
    st.pyplot(plt)

# Section: Sentiment Analysis
if options == "Sentiment Analysis":
    st.subheader("Sentiment Analysis Distribution")
    sentiment_counts = df['category'].value_counts()
    st.bar_chart(sentiment_counts)

# Section: Top Words
if options == "Top Words":
    st.subheader("Top Words")
    top_words = pd.Series(' '.join(df['cleaned_text']).split()).value_counts()[:10]
    st.bar_chart(top_words)

# Section: Most Recent Tweet
if options == "Most Recent Tweet":
    st.subheader("Most Recent Tweet")
    if not df.empty:
        recent_tweet = df.iloc[-1]['cleaned_text']
        st.write(recent_tweet)

# Footer
st.sidebar.write("Developed by Wahyu Nur Cahyanto")
