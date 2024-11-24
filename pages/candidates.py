import streamlit as st
import pandas as pd
import os


st.header("Candidats")

    # Saisie des informations
st.subheader("Postulez à un emploi")
name = st.text_input("Nom")
age = st.number_input("Âge", min_value=18, max_value=99, step=1)
job = st.text_input("Poste souhaité")
resume = st.file_uploader("Téléchargez votre CV", type=["pdf", "docx"])

if st.button("Soumettre"):
        if name and age and job and resume:
            # Sauvegarder les données
            data = {"Nom": name, "Âge": age, "Poste souhaité": job}
            df = pd.DataFrame([data])
            
            # Sauvegarder en mode append
            file_path = "data/candidates.csv"
            if not os.path.exists(file_path):
                df.to_csv(file_path, mode="w", header=True, index=False)
            else:
                df.to_csv(file_path, mode="a", header=False, index=False)

            st.success("Candidature soumise avec succès !")
        else:
            st.error("Veuillez remplir tous les champs.")

    # Consultation des résultats
st.subheader("Consultez vos résultats")
if st.button("Afficher les résultats"):
        try:
            df = pd.read_csv("data/candidates.csv")
            st.dataframe(df)
        except FileNotFoundError:
            st.error("Aucune donnée disponible pour le moment.")
