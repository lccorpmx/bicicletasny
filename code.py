import streamlit as st
import pandas as pd
import numpy as np

st.title('Recorridos de bicicletas en NYC AZR')

DATE_COLUMN = 'started_at'
DATA_URL = ('citibike-tripdata.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Cargando Bicicletas en new york')
data = load_data(1000)


st.image("credencial.png", width=150)
st.write("Nombre: Arturo Zilli Rios")
st.write("Correo: zs19004883@estudiantes.uv.mx")


if st.sidebar.checkbox('Mostrar data'):
    st.subheader('data')
    st.write(data)

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('# de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)


# Some number in the range 0-23
hour_to_filter = st.slider('Hora:', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa de la hora: %s:00' % hour_to_filter)
st.map(filtered_data)