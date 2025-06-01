
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import json

# ---------- Cargar JSON ----------
with open("sentiment_results.json", "r") as f:
    data = json.load(f)

tweets_df = pd.DataFrame(data["tweets"])
tweets_df["tweet_created"] = pd.to_datetime(tweets_df["tweet_created"])

# ---------- Título ----------
st.title("📊 Análisis de Sentimientos en Tweets sobre Aerolíneas")

st.markdown("""
Esta aplicación analiza más de 200 tweets relacionados con aerolíneas, clasificándolos en **positivos**, **negativos** o **neutrales** utilizando técnicas de Procesamiento de Lenguaje Natural (PLN).
""")

# ---------- Estadísticas Generales ----------
st.subheader("📈 Estadísticas Generales")
summary = data["summary"]
col1, col2, col3 = st.columns(3)

col1.metric("Positivos", summary["count"]["positive"], f'{summary["percentage"]["positive"]:.2f}%')
col2.metric("Negativos", summary["count"]["negative"], f'{summary["percentage"]["negative"]:.2f}%')
col3.metric("Neutrales", summary["count"]["neutral"], f'{summary["percentage"]["neutral"]:.2f}%')

# ---------- Imagen: Gráfico de barras ----------
st.subheader("📊 Porcentaje de Comentarios por Sentimiento")
st.image("grafico_porcentaje_sentimiento.png", caption="Distribución porcentual", use_container_width=True)

# ---------- Filtros ----------
st.subheader("🧰 Filtros Interactivos")

sent_filter = st.selectbox("Filtrar por sentimiento:", ["Todos", "positive", "negative", "neutral"])
date_min = tweets_df["tweet_created"].min().date()
date_max = tweets_df["tweet_created"].max().date()

start_date = st.date_input("Fecha inicio:", date_min, min_value=date_min, max_value=date_max)
end_date = st.date_input("Fecha fin:", date_max, min_value=date_min, max_value=date_max)

filtered = tweets_df[
    (tweets_df["tweet_created"].dt.date >= start_date) &
    (tweets_df["tweet_created"].dt.date <= end_date)
]

if sent_filter != "Todos":
    filtered = filtered[filtered["sentiment"] == sent_filter]

# ---------- Mostrar Tweets filtrados ----------
st.subheader("📝 Tweets Filtrados")
st.dataframe(filtered[["tweet_created", "clean_text", "sentiment"]])

# ---------- Imagen: Serie temporal ----------
st.subheader("📅 Evolución Temporal de Sentimientos")
st.image("serie_temporal_sentimientos.png", use_container_width=True)

# ---------- Imágenes: Nubes de palabras ----------
st.subheader("☁️ Nube de Palabras por Sentimiento")

col_pos, col_neu, col_neg = st.columns(3)
with col_pos:
    st.image("wordcloud_positive.png", caption="Positivos")
with col_neu:
    st.image("wordcloud_neutral.png", caption="Neutrales")
with col_neg:
    st.image("wordcloud_negative.png", caption="Negativos")

# ---------- Documentación In Situ ----------
st.subheader("📄 Documentación del Proyecto")

st.markdown("""
**Origen del Dataset:**  
Tweets recopilados de usuarios reales entre el 21 y 24 de febrero de 2015, enfocados en experiencias con aerolíneas.

**Preprocesamiento del Texto:**  
- Conversión a minúsculas  
- Eliminación de signos de puntuación y menciones  
- Lematización con NLTK  
- Clasificación de sentimiento usando VADER

**Modelo de Sentimiento:**  
El modelo **VADER** (Valence Aware Dictionary and sEntiment Reasoner) fue utilizado para puntuar cada tweet como `positivo`, `neutral` o `negativo`.

**Visualizaciones:**  
- Gráfico de barras con porcentajes de cada sentimiento.  
- Serie temporal de ocurrencias por sentimiento.  
- Nubes de palabras por categoría de sentimiento.

**Interpretación:**  
- La mayoría de los tweets fueron positivos, aunque hubo también una proporción significativa de comentarios negativos.  
- Las nubes muestran términos característicos de cada sentimiento (e.g., “help” y “thank” en positivos, “delayed” y “cancelled” en negativos).

**Limitaciones:**  
- Los modelos pueden fallar ante ironía o sarcasmo.  
- El contexto limitado de un tweet puede llevar a errores de clasificación.
""")
