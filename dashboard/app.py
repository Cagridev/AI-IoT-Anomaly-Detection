import streamlit as st
import requests
import pandas as pd
import time


API_URL = "http://127.0.0.1:8000/predict"


st.set_page_config(
    page_title="AI IoT Anomaly Detection",
    layout="wide"
)


st.title("🤖 AI IoT Anomaly Detection Dashboard")

st.write(
    "Real-time industrial machine monitoring system"
)


# Data storage

temperature = []
vibration = []
scores = []
anomalies = []


temp_chart = st.empty()
vibration_chart = st.empty()
score_chart = st.empty()

status_box = st.empty()
metrics_box = st.empty()

table_box = st.empty()


for i in range(100):

    sensor_data = {

        "temperature": st.session_state.get(
            "temperature",
            60 + i % 40
        ),

        "pressure": 30,

        "vibration": round(
            0.2 + (i % 10) / 10,
            2
        ),

        "speed": 1500,

        "power": 20

    }


    response = requests.post(
        API_URL,
        json=sensor_data
    )


    result = response.json()


    temperature.append(
        sensor_data["temperature"]
    )

    vibration.append(
        sensor_data["vibration"]
    )

    scores.append(
        result["score"]
    )

    anomalies.append(
        result["anomaly"]
    )


    # STATUS

    with status_box.container():

        if result["anomaly"] == -1:
            st.error(
                "🔴 ANOMALY DETECTED"
            )

        else:
            st.success(
                "🟢 MACHINE NORMAL"
            )


        st.write(
            "Reason:",
            result["reason"]
        )


    # METRICS

    with metrics_box.container():

        col1, col2, col3 = st.columns(3)


        with col1:
            st.metric(
                "Total Samples",
                len(anomalies)
            )


        with col2:
            st.metric(
                "Anomalies",
                anomalies.count(-1)
            )


        with col3:
            st.metric(
                "Normal",
                anomalies.count(1)
            )


    # Charts

    df = pd.DataFrame(
        {
            "Temperature": temperature
        }
    )


    temp_chart.line_chart(df)



    vib_df = pd.DataFrame(
        {
            "Vibration": vibration
        }
    )


    vibration_chart.line_chart(
        vib_df
    )



    score_df = pd.DataFrame(
        {
            "Anomaly Score": scores
        }
    )


    score_chart.line_chart(
        score_df
    )


    # Table

    latest = pd.DataFrame(
        [
            {
                "Temperature":
                sensor_data["temperature"],

                "Vibration":
                sensor_data["vibration"],

                "Speed":
                sensor_data["speed"],

                "Power":
                sensor_data["power"],

                "Result":
                result["anomaly"]
            }
        ]
    )


    table_box.dataframe(
        latest
    )


    time.sleep(2)