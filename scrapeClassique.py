import streamlit as st 
from scrape import scrape_website, split_dom_content, cleaned_body_content, extract_body_content
from parse import parse_with_ai
import asyncio



url = st.text_input("Enter the website URL : ")

if st.button ("Scrape Site"):
    st.write("Scraping the site...")


    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = cleaned_body_content(body_content)

    st.session_state.dom_content = cleaned_content    #creation d'une variable de session pour stocker le contenu nettoyé sous le nom dom_content
    
    with st.expander ("View DOM content"):
        st.text_area("DOM_content", cleaned_content, height= 300)

if "dom_content" in st.session_state:
    parse_description = st.text_area ("Describe what you want to parse")

    if st.button ("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = asyncio.run(parse_with_ai(dom_chunks, parse_description))
            st.write(parsed_result)
