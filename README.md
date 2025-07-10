#  Student Math Score Predictor

A simple Machine Learning + Streamlit app that predicts a student's **math exam score** based on their background and test preparation details.

Live App: [Click here to try it out!](https://student-math-score-predictor.streamlit.app)

---

Features

* Predicts math scores using a trained **Random Forest Regression** model
* Clean, interactive **Streamlit** UI
* Trained on real exam data from Kaggle
* Hosted on **Streamlit Cloud** and (coming soon) **AWS EC2**

---

Inputs Used

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type (standard or free/reduced)
* Test Preparation Course (completed or not)

---

 Model Details

* Algorithm: Random Forest Regressor (sklearn)
* Trained on: [Student Performance Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
* Saved as: `model.pkl` using `joblib`

---

How to Run Locally

1. Clone this repo:

   ```bash
   git clone https://github.com/yamini393/Student-Math-Score-Predictor.git
   cd Student-Math-Score-Predictor
   ```
