# sentiment-analysis-webapp

# ✈️ Análisis de Sentimientos en Tweets sobre Aerolíneas

Esta aplicación web analiza más de 200 tweets reales sobre aerolíneas, clasificándolos como **positivos**, **negativos** o **neutrales** usando técnicas de Procesamiento de Lenguaje Natural (PLN).

---

## 🚀 Demo en Vivo

Una vez desplegada en Streamlit Cloud, puedes acceder a la app aquí:

🔗 [Ver app en Streamlit](https://TU_USUARIO.streamlit.app)

---

## 📁 Contenido del Proyecto

- `app.py`: Código principal de la aplicación Streamlit.
- `sentiment_results.json`: Archivo con los datos preprocesados y resultados del análisis.
- `grafico_porcentaje_sentimiento.png`: Gráfico de distribución de sentimientos.
- `serie_temporal_sentimientos.png`: Evolución temporal de los sentimientos.
- `wordcloud_positive.png`, `wordcloud_neutral.png`, `wordcloud_negative.png`: Nubes de palabras por sentimiento.
- `requirements.txt`: Dependencias para ejecutar la app localmente.

---

## 🧰 Requisitos para Ejecutar Localmente

```bash
git clone https://github.com/TU_USUARIO/sentiment-analysis-webapp.git
cd sentiment-analysis-webapp
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧪 Técnicas y Herramientas Usadas

- **Preprocesamiento**: limpieza de texto, eliminación de `stopwords`, lematización.
- **Modelo de sentimiento**: [`VADER`](https://github.com/cjhutto/vaderSentiment), ideal para texto informal como tweets.
- **Visualización**: `matplotlib`, `Streamlit`, `wordcloud`.
- **Plataforma**: Desarrollado con `Python` y desplegado con `Streamlit Cloud`.

---

## 📊 Resultados y Análisis

- Se observó una alta proporción de tweets positivos, aunque también hay una presencia significativa de comentarios negativos.
- Las nubes de palabras muestran los términos más comunes por tipo de sentimiento.
- La serie temporal permite observar patrones a lo largo del tiempo.

---

## ⚠️ Limitaciones

- Los modelos de PLN simples pueden fallar ante ironía, sarcasmo o ambigüedad.
- El contexto de un tweet suele ser limitado.

---

## 📌 Créditos

Este proyecto fue desarrollado como parte de una tarea académica sobre análisis de sentimientos y visualización de datos.

---

© 2025 - Análisis de Sentimientos con Streamlit
