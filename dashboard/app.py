import streamlit as st
import requests
import time

st.set_page_config(
    page_title="Apex Store Intelligence",
    layout="wide"
)

st.title("🏪 Apex Store Intelligence Dashboard")

store_id = "STORE_BLR_002"

placeholder = st.empty()

while True:

    try:

        metrics = requests.get(
            f"http://127.0.0.1:8000/stores/{store_id}/metrics"
        ).json()

        with placeholder.container():

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Visitors",
                metrics.get(
                    "unique_visitors",
                    0
                )
            )

            col2.metric(
                "Avg Dwell",
                round(
                    metrics.get(
                        "avg_dwell_ms",
                        0
                    ) / 1000,
                    1
                )
            )

            col3.metric(
                "Queue Depth",
                metrics.get(
                    "queue_depth",
                    0
                )
            )

            col4.metric(
                "Conversion",
                metrics.get(
                    "conversion_rate",
                    0
                )
            )

    except Exception as e:

        st.error(str(e))

    time.sleep(3)