import math
import random
import numpy as np
import pandas as pd

#RANDOM DATA GENERATION

def reload():

    def generate_light_flux(intensity_min=100, intensity_max=1000, area_min=1, area_max=10, angle_min=0, angle_max=90):
        intensity = random.uniform(intensity_min, intensity_max)
        area = random.uniform(area_min, area_max)
        angle = random.uniform(angle_min, angle_max)
        angle_rad = math.radians(angle)
        flux = intensity * area * math.cos(angle_rad)
        return flux

    def generate_aqi():
        pm25 = random.uniform(0, 500)  # PM2.5 concentration in µg/m³
        o3 = random.uniform(0, 500)    # Ozone concentration in µg/m³
        no2 = random.uniform(0, 300)   # Nitrogen Dioxide concentration in µg/m³
        co = random.uniform(0, 50)     # Carbon Monoxide concentration in µg/m³

        aqi_pm25 = min(500, max(0, int((pm25 / 500) * 500))) # AQI for PM2.5
        aqi_o3 = min(500, max(0, int((o3 / 500) * 500)))     # AQI for Ozone
        aqi_no2 = min(500, max(0, int((no2 / 300) * 500)))   # AQI for NO2
        aqi_co = min(500, max(0,  int((co / 50) * 500)))     # AQI for CO
        aqi = max(aqi_pm25, aqi_o3, aqi_no2, aqi_co)
        return round(aqi, 2)

    data = {
        "Timestamp": pd.date_range(start="2025-02-26 10:00", periods=20, freq="0.5h"),
        "Temperature(°C)": np.random.uniform(15, 50, 20),
        "Humidity (%)": np.random.uniform(10, 100, 20),
        "Light Intensity (lux)": np.random.uniform(generate_light_flux() , size = 20),
        "Air Quality (ppm)": (np.random.uniform(generate_aqi() , size = 20)),
    }

    csv_file = "sensor_test_data.csv"
    df = pd.DataFrame.from_dict(data)
    df.to_csv(csv_file, index=False)

    return df
