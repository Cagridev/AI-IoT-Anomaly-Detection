import pandas as pd
from sklearn.ensemble import IsolationForest


data = pd.read_csv("../data/machine_data.csv")

features = ["temperature", "pressure", "vibration", "speed", "power"]

model = IsolationForest(
    contamination=0.1,
    random_state=42
)

model.fit(data[features])

data["anomaly"] = model.predict(data[features])

data["score"] = model.decision_function(data[features])


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


data["reason"] = data.apply(explain, axis=1)

print(data)