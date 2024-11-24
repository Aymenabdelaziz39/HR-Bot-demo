import streamlit as st
import pandas as pd
import os


st.header("Recruteurs")

    # Création d'offres d'emploi
st.subheader("Créer une offre d'emploi")
job_title = st.text_input("Titre du poste")
job_desc = st.text_area("Description du poste")

if st.button("Publier l'offre"):
        if job_title and job_desc:
            # Sauvegarder les données
            data = {"Poste": job_title, "Description": job_desc}
            df = pd.DataFrame([data])
            
            # Sauvegarder en mode append
            file_path = "data/jobs.csv"
            if not os.path.exists(file_path):
                df.to_csv(file_path, mode="w", header=True, index=False)
            else:
                df.to_csv(file_path, mode="a", header=False, index=False)

            st.success("Offre d'emploi créée avec succès !")
        else:
            st.error("Veuillez remplir tous les champs.")

    # Vérification des candidatures
st.subheader("Consulter les candidatures")
if st.button("Afficher les candidatures"):
        try:
            df = pd.read_csv("data/candidates.csv")
            st.dataframe(df)
        except FileNotFoundError:
            st.error("Aucune candidature disponible.")    
