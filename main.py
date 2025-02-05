import streamlit as st 
from scrape import scrape_website, split_dom_content, cleaned_body_content, extract_body_content

st.title("Ai scraper Web")
url = st.text_input("Enter the website URL : ")

if st.button ("Scrape Site"):
    st.write("Scraping the site")


    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = cleaned_body_content(body_content)

    st.session_state.dom_content = cleaned_content    #creation d'une variable de session pour stocker le contenu nettoyé sous le nom dom_content
    
    with st.expander ("View DOM content"):
        st.text_area("DOM_content", cleaned_content, height= 300)