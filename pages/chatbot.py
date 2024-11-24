import random
import time
import streamlit as st

# Streamed response emulator
def response_generator(prompt):
    # Réponses personnalisées pour améliorer le CV
    response = random.choice(
        [
            "Salut ! Comment puis-je t'aider à améliorer ton CV ?",
            "Bonjour ! Est-ce que tu as des questions spécifiques sur ton CV ?",
            "Hello ! Tu veux des conseils pour ton CV ou pour la recherche d'emploi ?",
            "Salut ! Si tu veux de l'aide pour ton CV, je suis là pour ça.",
            "Bonjour ! Dis-moi ce que tu aimerais améliorer sur ton CV.",
            "Salut ! Comment puis-je t'aider à rendre ton CV plus attractif ?",
        ]
    )

    # Personnalisation de la réponse selon la demande de l'utilisateur
    if "expérience" in prompt.lower():
        response = "Super ! Pour l'expérience, il est important de détailler tes réalisations, pas seulement tes responsabilités. N'oublie pas d'inclure des chiffres quand c'est possible !"
    elif "compétences" in prompt.lower():
        response = "Les compétences doivent être présentées clairement. Pense à séparer les compétences techniques et les compétences humaines. Quelles compétences as-tu acquises ?"
    elif "formation" in prompt.lower():
        response = "Il est important de mentionner ta formation, mais aussi les projets réalisés durant cette période. Ça peut être très attractif pour les recruteurs."
    elif "recherche" in prompt.lower():
        response = "Tu cherches un emploi spécifique ? Ou tu veux juste des conseils généraux sur la rédaction de CV et les entretiens ?"
    elif "moi" in prompt.lower():
        response = "Tu as déjà une version de ton CV ou tu souhaites que je t'aide à en créer un ?"
    
    return response

st.title("HR Bot")

# Initialisation de l'historique de la conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages précédents
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Acceptation de l'entrée utilisateur
if prompt := st.chat_input("Comment puis-je t'aider à améliorer ton CV ?"):
    # Ajouter le message de l'utilisateur à l'historique de la conversation
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Afficher le message de l'utilisateur
    with st.chat_message("user"):
        st.markdown(prompt)

    # Afficher la réponse du chatbot sans effet de répétition
    with st.chat_message("assistant"):
        response = response_generator(prompt)
        st.markdown(response)  # Affichage de la réponse complète

    # Ajouter la réponse du chatbot à l'historique
    st.session_state.messages.append({"role": "assistant", "content": response})
