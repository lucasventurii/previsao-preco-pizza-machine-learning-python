import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

# ======================
# Carregando dados
# ======================

df = pd.read_csv("pizzas.csv")

# ======================
# Treinando modelo
# ======================

x = df[["diametro"]]
y = df[["preco"]]

modelo = LinearRegression()
modelo.fit(x, y)

# ======================
# Interface
# ======================

st.title("🍕 Prevendo o valor da pizza")

diametro = st.number_input(
    "Digite o diâmetro da pizza (cm)",
    min_value=10.0,
    max_value=100.0,
    step=1.0
)

if st.button("Prever preço"):

    preco_previsto = modelo.predict([[diametro]])[0][0]

    st.success(
        f"Pizza de {diametro:.1f} cm custa R$ {preco_previsto:.2f}"
    )