import streamlit as st


secao_usuario = st.session_state
usuario = secao_usuario.name

left_column, right_column = st.columns([1, 2])
left_column.title("ImpressiveApp")

left_column.write(f"""
#### Bem Vindo Impressionador {usuario}
""")

button_dashboard = left_column.button("Project Dashboard")
button_indicators = left_column.button("Main Indicators")
if button_dashboard:
    st.switch_page("dashboard.py")
if button_indicators:
    st.switch_page("indicator.py")

container = right_column.container(border=True)
container.image("images/time-comunidade.webp")
