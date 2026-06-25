from fastapi import FastAPI
import pandas as pd
from sklearn.ensemble import IsolationForest

app = FastAPI()

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "machine_data.csv")

data = pd.read_csv(file_path)

features = ["temperature", "pressure", "vibration", "speed", "power"]

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(data[features])


def explain(row):
    reasons = []

    if row["temperature"] > 80:
        reasons.append("High temperature spike")

    if row["vibration"] > 1.0:
        reasons.append("Abnormal vibration")

    if row["speed"] < 1000:
        reasons.append("Speed drop detected")

    if len(reasons) == 0:
        return "Normal operating conditions"

    return ", ".join(reasons)


@app.post("/predict")
def predict(sensor: dict):
    df = pd.DataFrame([sensor])

    anomaly = model.predict(df[features])[0]
    score = model.decision_function(df[features])[0]
    reason = explain(df.iloc[0])

    return {
        "anomaly": int(anomaly),
        "score": float(score),
        "reason": reason
    }