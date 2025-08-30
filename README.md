# ML-Project-Simple-Linear-Regression-with-streamlit
## 📚 Student Performance Predictor
This web app uses a machine learning model to predict a student's Performance Index based on key academic and lifestyle inputs. Built with Streamlit, it provides an intuitive interface for educators, students, or analysts to explore how factors like study hours, sleep, previous scores, and extracurricular activities influence performance.
### 🔍 Features
- Input fields for:
- Hours Studied
- Previous Scores
- Sleep Hours
- Sample Question Papers Practiced
- Extracurricular Activities
- Real-time prediction using a trained ElasticNet regression model
- Scaled input processing via StandardScaler
- Clean UI with interactive controls
- Ready for deployment on Streamlit Cloud
🧠 Tech Stack
- Python
- scikit-learn
- Streamlit
- NumPy, Pandas, Matplotlib, Seaborn
🚀 How It Works
- User enters student data
- Inputs are scaled using a saved scaler.pkl
- Model (finalmodel.pkl) predicts the performance index
- Result is displayed instantly
