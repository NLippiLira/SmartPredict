# 🚀 SmartPredict

SmartPredict is a full-stack Machine Learning web application that predicts credit approval based on user input data such as age, income, and credit score.

The project demonstrates a complete real-world workflow including model training, API development, frontend integration, Dockerization, and cloud deployment.

---

## 🌐 Live Demo

- Frontend: https://nlippilira.github.io/SmartPredict/
- Backend API: https://YOUR-RENDER-URL.onrender.com

---

## 🧠 Features

- 📊 Machine Learning model using Scikit-learn
- ⚡ REST API built with Flask
- 🎨 Interactive frontend using HTML, CSS, JavaScript
- 🐳 Dockerized backend for portability
- ☁️ Deployed in the cloud (Render + GitHub Pages)
- 🔗 Real-time predictions via API

---

## 🏗️ Project Structure


smartpredict/
│
├── backend/
│ ├── model/
│ │ └── model.pkl
│ ├── model/
│ │ └── train.py
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── index.html
├── styles.css
├── app.js
│
└── README.md


---

## ⚙️ Tech Stack

### Backend
- Python 3.10
- Flask
- Scikit-learn
- Pandas
- Joblib

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)

### DevOps
- Docker
- GitHub Pages
- Render

---

## 🚀 Getting Started (Local Setup)

### 1. Clone repository

```bash
git clone https://github.com/YOUR-USER/smartpredict.git
cd smartpredict
2. Setup backend
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
3. Train model
python model/train.py
4. Run API
python app.py
5. Open frontend

Open index.html in your browser.

🐳 Docker Usage
Build image
docker build -t smartpredict-api .
Run container
docker run -p 5000:5000 smartpredict-api
🔌 API Usage
Endpoint
POST /predict
Example request
{
  "edad": 30,
  "ingresos": 500000,
  "score": 700
}
Example response
{
  "prediccion": 1
}
🌍 Deployment
Frontend deployed on GitHub Pages
Backend deployed using Docker on Render
🤖 Future Improvements
Add authentication system
Improve model accuracy with real dataset
Add database integration
CI/CD pipeline with GitHub Actions
UI improvements with modern frameworks (React)
👨‍💻 Author

Nicolás Lippi

Full Stack Developer
Machine Learning Enthusiast
