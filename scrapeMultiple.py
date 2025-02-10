import streamlit as st
from googleGrab import google_search_results

st.title("Google Search Scraper")

subject = st.text_input("Enter the subject you want to search for:")

if st.button("Search"):
    st.write("🔍 Searching for results...")
    
    result = google_search_results(subject)
    
    if result:
        st.success(f"Found {len(result)} results!")
        st.session_state["search_results"] = result  # Sauvegarde des résultats en session
    else:
        st.error("No results found. Google might be blocking the scraper.")
        st.session_state["search_results"] = []

if "search_results" in st.session_state and st.session_state["search_results"]:
    if st.checkbox("Show results"):
        for link in st.session_state["search_results"]:
            st.markdown(f"[🔗 {link}]({link})")