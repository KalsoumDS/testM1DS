# app.py
import streamlit as st

st.title("📝 Mon Formulaire Simple")

with st.form("mon_formulaire"):
    st.header("Informations personnelles")
    
    nom = st.text_input("Nom complet*")
    email = st.text_input("Email*")
    age = st.number_input("Âge", min_value=0, max_value=120)
    profession = st.selectbox(
        "Profession",
        ["Étudiant", "Développeur", "Designer", "Autre"]
    )
    message = st.text_area("Votre message")
    
    newsletter = st.checkbox("Je souhaite m'abonner à la newsletter")
    
    submitted = st.form_submit_button("Soumettre")
    
    if submitted:
        if not nom or not email:
            st.error("Veuillez remplir les champs obligatoires (*)")
        else:
            st.success("Formulaire soumis avec succès!")
            st.write("### Récapitulatif:")
            st.write(f"- Nom: {nom}")
            st.write(f"- Email: {email}")
            st.write(f"- Âge: {age}")
            st.write(f"- Profession: {profession}")
            st.write(f"- Message: {message}")
            st.write(f"- Newsletter: {'Oui' if newsletter else 'Non'}")
