# Cuadro de Mandos - Análisis de Vehículos 🚗📊  

Esta aplicación web, desarrollada con **Streamlit**, permite visualizar y analizar datos de anuncios de venta de vehículos en EE.UU. Utiliza **Plotly** para generar gráficos interactivos y facilita la exploración del conjunto de datos.  

URL para acceder al proyecto en Render: https://vehicles-env-6r1b.onrender.com

## 📌 Funcionalidades  
✅ Visualización de un **histograma del odómetro** para analizar la distribución del kilometraje de los vehículos.  
✅ **Gráfico de dispersión** que relaciona el precio y el odómetro, permitiendo identificar tendencias en los datos.  
✅ Interfaz intuitiva con **casillas de verificación** para elegir qué gráficos mostrar.  

## 🚀 Cómo ejecutar la aplicación  
1. Asegúrate de tener **Python** instalado.  
2. Instala las dependencias ejecutando:  
   pip install streamlit pandas plotly
3. Corre la aplicacion con el siguiente comando
   streamlit run app.py

## 🌍 Despliegue en Render

Para hacer compatible la aplicación con Render, incluye un archivo de configuración en streamlit/config.toml con el siguiente contenido:

[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000

## 📂 Estructura del proyecto

/proyecto  
│── app.py               # Código de la aplicación Streamlit  
│── vehicles_us.csv      # Conjunto de datos  
│── README.md            # Descripción del proyecto  
│── requirements.txt     # Dependencias  
│── streamlit/config.toml # Configuración para Render

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue en el repositorio. 🚀
