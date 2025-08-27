import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from  models import Usuario, session


user_list = session.query(Usuario).all()


credenciais = {
"usernames": {usuario.email:{"name": usuario.name, "password": usuario.senha} for usuario in user_list}
}

authenticator = stauth.Authenticate(credenciais, "app_cookies", "1&2&3&4&5&6&7&#%#", cookie_expiry_days=10)
#authenticator.authentication_controller
def authenticate_user(authenticator):
    name, status_auth, username = authenticator.login()
    if status_auth:
        st.toast("Login realizado com sucesso!", icon="✅")
        return {"name": name, "username": username}
    elif status_auth == False:
        st.error("Dados Invalidos...Preencha Novamente")
    else:
        st.error("Preencha os Campos Corretamente")

def logout_user():
    authenticator.logout()

user_data = authenticate_user(authenticator)

if user_data:
    email_usuario = user_data["username"]
    admin = session.query(Usuario).filter_by(email=email_usuario, admin=True).first()

    if admin:
        pages = st.navigation({
            "Home": [st.Page("home.py", title="Pinheiro Impressionador")],
            "Dashboards": [st.Page("dashboard.py", title="Dashboard"), st.Page("indicator.py", title="Indicators")],
            "Conta": [st.Page("create_account.py", title="Criar Conta"), st.Page(logout_user, title="Sair")]
        })
    else:
        pages = st.navigation({
            "Home": [st.Page("home.py", title="Pinheiro Impressionador")],
            "Dashboards": [st.Page("dashboard.py", title="Dashboard"), st.Page("indicator.py", title="Indicators")],
            "Conta": [st.Page(logout_user, title="Sair")]
        })

    pages.run()


