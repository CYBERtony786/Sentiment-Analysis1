import streamlit as st
from textblob import TextBlob

# 1. UI Setup (Website ka header)
st.title("🧠 AI Mood Detector")
st.write("Koi bhi English sentence likhein aur AI aapka mood batayega!")

# 2. User se input lena
user_text = st.text_input("Aapka sentence yahan likhein:")

# 3. Button lagana
if st.button("Analyze Mood"):
    
    # Check karna ki user ne box khali toh nahi chhod diya
    if user_text == "":
        st.error("Pehle kuch likhiye toh sahi!")
    else:
        # AI Brain ko bulana
        blob = TextBlob(user_text)
        score = blob.sentiment.polarity
        
        # Result ko screen par dikhana
        if score > 0:
            st.success(f"AI Result: POSITIVE 😃 (Score: {score:.2f})")
        elif score < 0:
            st.error(f"AI Result: NEGATIVE 😠 (Score: {score:.2f})")
        else:
            st.warning("AI Result: NEUTRAL 😐 (Score: 0.0)")