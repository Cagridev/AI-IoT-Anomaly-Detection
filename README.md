# AI-Based IoT Anomaly Detection System

This project is a Machine Learning-based anomaly detection system for industrial IoT sensor data.  
It detects abnormal machine behavior using Isolation Forest and exposes predictions via FastAPI.

---

## 🚀 Project Overview

The system analyzes sensor data from industrial machines:

- Temperature
- Pressure
- Vibration
- Speed
- Power

It detects anomalies and returns:

- Normal / Anomaly result
- Risk score
- Human-readable explanation

---

## 🧠 Machine Learning Model

We use Isolation Forest (unsupervised learning).

It learns normal patterns and detects deviations.

---

## 📡 API Endpoint

POST /predict

---

## 📡 Input Format

Send JSON like this:

{
  "temperature": 95,
  "pressure": 60,
  "vibration": 2.5,
  "speed": 700,
  "power": 55
}

---

## 📡 Output Format

{
  "anomaly": -1,
  "score": -0.31,
  "reason": "High temperature spike, Abnormal vibration, Speed drop detected"
}

---

## 📌 Field Explanation

anomaly = 1 (normal), -1 (anomaly)  
score = how abnormal the data is  
reason = explanation of the anomaly

---

## 🛠 Tech Stack

- Python  
- FastAPI  
- Pandas  
- Scikit-learn  
- Uvicorn  

---

## 📁 Project Structure

AI-IoT-Anomaly-Detection/
├── data/
│   └── machine_data.csv
├── model/
│   └── api.py
├── requirements.txt
└── README.md

---

## ▶️ Run Project

pip install -r requirements.txt  
uvicorn model.api:app --reload  

Open: http://127.0.0.1:8000/docs