import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Analisis de precios de autos')

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma') #crear boton histograma
scatter_button = st.button('Construir grafico de dispersion') #crear boton scatter
if hist_button: #si presiona el boton
    #da un histograma
    st.write('Histograma de precios')
    #crear histograma
    fig = px.histogram(car_data, x="odometer", title='millas recorridas')
    #Mostrar plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


#crear scatter plot
if scatter_button:
    st.write('Grafico de dispersion')
    dispersion = px.scatter(car_data, x='model_year', y='price', title='Precio vs Año')
    st.plotly_chart(dispersion, use_container_width=True)


