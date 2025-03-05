import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

import data


def main():
    df = pd.read_csv('sensor_test_data.csv')
    test_data = df
    last_row = test_data.tail(1)
    last_temp = last_row['Temperature(°C)']
    last_humidity = last_row['Humidity (%)']
    last_light_int = last_row['Light Intensity (lux)']
    last_air_quality = last_row['Air Quality (ppm)']

    display_header()

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        plot_gauge(int(last_temp.iloc[0]), "green", "°C", "Температура", 50)  # Example: Temperature Gauge
    with col2:
        plot_gauge(int(last_humidity.iloc[0]), "blue", "%", "Влажност", 100)  # Example: Humidity Gauge
    col3, col4 = st.columns(2)
    with col3:
        plot_gauge(int(last_light_int.iloc[0]), "orange", " lux", "Интензивност на светлина", 10000)  # Example: Light Intensity Gauge
    with col4:
        plot_gauge(int(last_air_quality.iloc[0]), "red", " ppm", "Честота на въздуха", 500)  # Example: Air Quality Gauge

    if st.sidebar.button("Генерирай нови данни"):
        test_data = data.reload()

    if st.sidebar.button("Изведи инфромацията"):
        st.dataframe(test_data)

    if st.sidebar.button("Изведи диаграми"):
        charts(test_data)

    display_footer()


def charts(test_data):
    # Plot Temperature over time
    st.write("### Температура (°C) - Време")
    fig, ax = plt.subplots()
    ax.plot(test_data['Timestamp'], test_data['Temperature(°C)'], marker='o', linestyle='-', color='r')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature vs Time')
    plt.xticks(rotation=90)
    st.pyplot(fig)
    # Plot Humidity over time
    st.write("### Валжност (%) - Време")
    fig, ax = plt.subplots()
    ax.plot(test_data['Timestamp'], test_data['Humidity (%)'], marker='o', linestyle='-', color='b')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Humidity (%)')
    ax.set_title('Humidity vs Time')
    plt.xticks(rotation=90)
    st.pyplot(fig)
    # Plot Light Intensity over time
    st.write("### Интензитет на светлината (lux) - Време")
    fig, ax = plt.subplots()
    ax.plot(test_data['Timestamp'], test_data['Light Intensity (lux)'], marker='o', linestyle='-', color='g')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Light Intensity (lux)')
    ax.set_title('Light Intensity vs Time')
    plt.xticks(rotation=90)
    st.pyplot(fig)
    # Plot Air Quality over time
    st.write("### Чистота на въздуха (ppm) - Време")
    fig, ax = plt.subplots()
    ax.plot(test_data['Timestamp'], test_data['Air Quality (ppm)'], marker='o', linestyle='-', color='purple')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Air Quality (ppm)')
    ax.set_title('Air Quality vs Time')
    plt.xticks(rotation=90)
    st.pyplot(fig)


def plot_gauge(indicator_number, indicator_color, indicator_suffix, indicator_title, max_bound):
    fig = go.Figure(
        go.Indicator(
            value=indicator_number,
            mode="gauge+number",
            domain={"x": [0, 1], "y": [0, 1]},
            number={
                "suffix": indicator_suffix,
                "font.size": 26,
            },
            gauge={
                "axis": {"range": [0, max_bound], "tickwidth": 1},
                "bar": {"color": indicator_color},
            },
            title={
                "text": indicator_title,
                "font": {"size": 28},
            },
        )
    )
    fig.update_layout(
        # paper_bgcolor="lightgrey",
        height=200,
        margin=dict(l=10, r=10, t=50, b=10, pad=8),
    )
    st.plotly_chart(fig, use_container_width=True)


def display_header():
    st.markdown(
        """
        <style>
        .header {
            font-size: 36px;
            color: #1E90FF;
            font-weight: bold;
            text-align: center;
            margin-top: 10px;
        }
        </style>
        <div class="header">
            Weather Data Dashboard 🌦️
        </div>
        """,
        unsafe_allow_html=True
    )


def display_footer():
    st.markdown(
        """
        <style>
        .footer {
            font-size: 14px;
            color: #A9A9A9;
            text-align: center;
            padding: 10px;
            margin-top: 20px;
        }
        </style>
        <div class="footer">
            Powered by WeatherApp | © 2025 WeatherApp
        </div>
        """,
        unsafe_allow_html=True
    )


# Run the app
if __name__ == "__main__":
    main()
