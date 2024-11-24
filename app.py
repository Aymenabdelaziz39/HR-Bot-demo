import streamlit as st


# --- PAGE SETUP ---
home_page = st.Page(
    "pages/acceuil.py",
    title="Acceuil",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "pages/candidates.py",
    title="Candidate",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "pages/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_3_page =st.Page(
    "pages/owner.py",
    title="Owner",
    icon=":material/smart_toy:",
)



# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Home": [home_page],
        "Projects": [project_1_page, project_2_page,project_3_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/Logo.png")


# --- RUN NAVIGATION ---
pg.run()



# Menu pour navigation

