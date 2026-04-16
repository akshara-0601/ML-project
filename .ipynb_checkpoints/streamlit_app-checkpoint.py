import streamlit as st
import requests

#page config 
st.set_page_config(
    page_title ="Sentiment Analysis",
    page_icon = "🎬",
    layout="centered"
)

st.title("🎬 Movie Review Sentiment Analyzer")
st.write("Enter a movie review and get instant sentiment prediction!")

# Input box
review = st.text_area("Enter your movie review here:", height=150)

# Predict button
if st.button("Analyze Sentiment"):
    if review.strip()=="":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            # call your flask backend
            response = requests.post(
                "http://127.0.0.1:5000/predict",
                json={"reviews": review}
            )
            result= response.json()

            # Display result
            sentiment = result['prediction']
            # confidence = result['confidence']

            if "pos" in sentiment or "neg" in sentiment:
                st.success(f"Sentiment : {sentiment}")
            else:
                st.error(f"Sentiment : {sentiment}")

            # st.metric(label="Confidence", value=confidence)
                