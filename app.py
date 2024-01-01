import streamlit as st
import joblib

model, vectorizer = joblib.load('.../news_classifier.joblib')

st.title('News Topic Classification')

new_article = st.text_area('Enter a news article')

new_article_tfidf = vectorizer.transform([new_article])

prediction = model.predict(new_article_tfidf)

if st.button('Submit'):
    st.subheader('Predicted Topic')
    st.write(prediction[0])
