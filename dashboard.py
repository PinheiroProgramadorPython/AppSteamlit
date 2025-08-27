import streamlit as st
from  data_loader import load_data
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


base = load_data()

left_column, center_column, right_column = st.columns([1,1,1])

setor = left_column.selectbox("Setor", base["Setor"].unique())
status = center_column.selectbox("Status", base["Status"].unique())

base = base[(base["Status"]==status) & (base["Setor"]==setor)]
base_mensal = base.groupby(base["Data Chegada"].dt.to_period("M")).sum(numeric_only=True).reset_index()
base_mensal["Data Chegada"] = base_mensal["Data Chegada"].dt.to_timestamp()

container = st.container(border=True)
with container:
    st.write("### Total de Projetos por Mês R$")
    grafic_area = px.area(base_mensal, x="Data Chegada", y="Valor Negociado")
    st.plotly_chart(grafic_area)

    left_column, right_column = st.columns([3, 1])

    left_column.write("### Comparação Orçado x Pago")

    base_mensal["Ano"] = base_mensal["Data Chegada"].dt.year
    list_year = base_mensal["Ano"].unique()
    year_select =  right_column.selectbox("Ano", list_year)

    base_mensal = base_mensal[base_mensal["Ano"]==year_select]
    total_pago = base_mensal["Valor Negociado"].sum()
    total_desconto = base_mensal["Desconto Concedido"].sum()

    left_column, right_column = st.columns([1, 1])
    left_column.metric("Total Pago", f"R${total_pago:,}")
    right_column.metric("Total Desconto", f"R${total_desconto:,}")

    # Criando Grafico de Barras com Plotly
    grafic_bar = go.Figure(data=[
        go.Bar(name="Valor Orçado", x=base_mensal["Data Chegada"], y=base_mensal["Valor Orçado"],
               text=base_mensal["Valor Orçado"]),
        go.Bar(name="Valor Pago", x=base_mensal["Data Chegada"], y=base_mensal["Valor Negociado"],
               text=base_mensal["Valor Negociado"])
    ])
    grafic_bar.update_layout(barmode="group")
    st.plotly_chart(grafic_bar)
