import streamlit as st
import pandas as pd
from data_loader import load_data


st.title("Main Indicators")

base = load_data()

def criar_card(icon, number, text, card_column):
    container = card_column.container(border=True)
    left_column, right_column = container.columns([1, 2.5])
    left_column.image(f"images/{icon}")
    right_column.write(number)
    right_column.write(text)


left_column, center_column, right_column = st.columns([1,1,1])

base_fechados = base[base["Status"].isin(["Em andamento", "Finalizado"])]
base_andamento = base[base["Status"] == "Em andamento"]

criar_card("oportunidades.png", f"{base['Código Projeto'].count()}", "Oportunidades", left_column)
criar_card("projetos_fechados.png", f"{base_fechados['Código Projeto'].count()}", "Projetos Fechados", center_column)
criar_card("em_andamento.png", f"{base_andamento['Código Projeto'].count()}", "Em Andamento", right_column)

criar_card("total_orcado.png", f"R${base_fechados['Valor Orçado'].sum():,}", "Total Orçado", left_column)
criar_card("total_pago.png", f"R${base_fechados['Valor Negociado'].sum():,}", "Total Pago", center_column)
criar_card("desconto.png", f"R${base_fechados['Desconto Concedido'].sum():,}", "Total Desconto", right_column)



import plotly.express as px

base_status = base.groupby("Status", as_index=False).count()
base_status = base_status.rename(columns={"Código Projeto": "Quantidade"})
base_status = base_status.sort_values(by="Quantidade", ascending=False)

#st.table(base_status.head(10))

grafic = px.funnel(base_status, x="Quantidade", y="Status")
st.plotly_chart(grafic)
