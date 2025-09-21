import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="favicon.png"
)

model = joblib.load('spam_classifier_nb_joblib.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("📧 Email Spam Detector")
st.write("You can type a single email or upload a CSV file to check multiple emails at once.")

email_input = st.text_area("Enter Email Text (Optional for single email prediction)")

uploaded_file = st.file_uploader("Upload CSV file with a column named 'Email'", type=["csv"])

if st.button("Check Single Email"):
    if email_input.strip() == "":
        st.warning("Please enter some email text!")
    else:
        email_vector = vectorizer.transform([email_input])
        prediction = model.predict(email_vector)[0]
        if prediction == 1:
            st.error("⚠️ This email is Spam!")
        else:
            st.success("✅ This email is Ham (Not Spam)")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if 'Email' not in df.columns:
            st.error("CSV must have a column named 'Email'")
        else:
            st.write("Predicting emails...")
            email_vectors = vectorizer.transform(df['Email'])
            predictions = model.predict(email_vectors)
            df['Prediction'] = ['Spam' if p==1 else 'Ham' for p in predictions]
            st.success("✅ Batch prediction completed!")
            st.dataframe(df)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Results as CSV",
                data=csv,
                file_name='spam_prediction_results.csv',
                mime='text/csv'
            )
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
