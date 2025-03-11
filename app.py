import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Analisis de precios de autos')

car_data = pd.read_csv('/Users/missa/LEARNING_PYTHON_LOCAL/PROYECT_SPRINT7/vehicles_us.csv')
hist_button = st.button('Construir histograma') #crear un boton

if hist_button: #si presiona el boton
    #da un histograma
    st.write('Histograma de precios')
    #crear histograma
    fig = px.histogram(car_data, x="odometer", title='millas recorridas')
    #Mostrar plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.write('Grafico de dispersion')
#crear scatter plot
if st.button('Construit grafico de dispersion'):
    dispersion = px.scatter(car_data, x='model_year', y='price', title='Precio vs Año')
    st.plotly_chart(dispersion, use_container_width=True)


