import emoji
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analysis", page_icon="🎯")
st.title("Sentiment Analysis")
raw_text = st.text_area("Enter Your Text")
if raw_text and st.button("Analyze"):
    blob = TextBlob(raw_text)
    result = blob.sentiment.polarity
    if result > 0.0:
        custom_emoji = ":smile:"
        st.subheader(emoji.emojize(custom_emoji))
    elif result < 0.0:
        custom_emoji = ":disappointed:"
        st.subheader(emoji.emojize(custom_emoji))
    else:
        st.subheader(emoji.emojize(":expressionless:"))
    st.info(f"Polarity Score is:: {result}")
