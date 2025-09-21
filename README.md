# 📧 Email Spam Detector

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-orange) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-green)

## 🌟 Project Overview
**Email Spam Detector** is a smart and interactive web app built using **Python, Scikit-learn, and Streamlit**.  
It classifies emails as **Spam** or **Not Spam (Ham)** using machine learning and natural language processing (NLP) techniques.  
Users can test single emails or bulk emails via CSV/Excel files.

## 🎬 Live Demo
Check the live site here: [Email Spam Detector Live](https://share.streamlit.io/333vaibhav/email-spam-detector)

## 💎 Features
- ✅ Classifies emails as **Spam** or **Not Spam**  
- ✅ Single email input or **bulk email classification**  
- ✅ Built using **Naive Bayes classifier** and **TF-IDF Vectorizer**  
- ✅ Interactive **Streamlit web app** with real-time results  
- ✅ Easy to extend with more ML models for better accuracy  

## 🖥️ Technologies Used
- **Python** – Programming language  
- **Scikit-learn** – Machine Learning library  
- **Streamlit** – Web app framework  
- **Pandas** – Data handling  
- **Joblib** – Model serialization  

## 📂 Project Structure
📦 email-spam-detector
 ┣ 📜 spam_detector_app.py
 ┣ 📜 spam_classifier_nb_joblib.pkl
 ┣ 📜 vectorizer.pkl
 ┣ 📜 spam_excel_file.xlsx
 ┣ 📜 requirements.txt
 ┗ 📜 README.md

## 🚀 How to Run Locally
1. Clone the repository:  
```bash
git clone https://github.com/333Vaibhav/email-spam-detector.git
cd email-spam-detector
Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run spam_detector_app.py

Open your browser at:

http://localhost:8501

🎯 Future Improvements

Add more ML models (Logistic Regression, SVM, etc.) for better accuracy

Deploy online (Streamlit Cloud / Heroku)

Enhance UI/UX for better user experience

Add advanced email preprocessing and NLP techniques

## 📸 Demo Screenshot
![Demo Screenshot](demo.png)

📜 License

This project is open-source and free to use.

✨ Author
Vaibhav Rathod
LinkedIn | GitHub
