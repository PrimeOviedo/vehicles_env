import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
data_path = "vehicles_us.csv"  # Asegúrate de que el archivo esté en el mismo directorio
car_data = pd.read_csv(data_path)

# Encabezado
title = "Cuadro de Mandos - Análisis de Vehículos"
st.header(title)

# Checkbox para mostrar histogramas y gráficos de dispersión
show_histogram = st.checkbox("Mostrar histograma del odómetro")
show_scatter = st.checkbox("Mostrar gráfico de dispersión de precio vs odómetro")

if show_histogram:
    st.write("Histograma del odómetro de los vehículos")
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write("Gráfico de dispersión de precio vs odómetro")
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro", opacity=0.5)
    st.plotly_chart(fig_scatter, use_container_width=True)
