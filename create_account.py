import streamlit as st
from models import Usuario, session
import streamlit_authenticator as stauth


form = st.form("Form_Create_Account")
name_digtado = form.text_input("Name")
email_digitado = form.text_input("Email")
senha_digitado = form.text_input("Senha", type="password")
admin_digitado = form.checkbox("Admin")
button_submit = form.form_submit_button("Enviar")

user_list = session.query(Usuario).filter_by(email=email_digitado).all()

if button_submit:
    if len(user_list) > 0:
        st.write("Email ja Existente...Digite outro...")
    else:
        password = stauth.Hasher([senha_digitado]).generate()[0]
        usuario = Usuario(name=name_digtado, email=email_digitado, senha=password, admin=admin_digitado)
        session.add(usuario)
        session.commit()
        st.toast("Usuario criado com Sucesso!", icon="✅")
        st.switch_page("home.py")
