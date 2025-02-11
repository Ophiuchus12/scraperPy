import asyncio
import streamlit as st
from googleGrab import google_search_results
from scrape import scrape_website, extract_body_content, cleaned_body_content, split_dom_content
from parse import parse_with_ai

st.title("Google Search Scraper")

if "search_results" not in st.session_state:
    st.session_state["search_results"] = []

if "dom_content" not in st.session_state:
    st.session_state["dom_content"] = ""

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


if st.session_state["search_results"]:
    if st.button("Get Content") :
        for url in st.session_state["search_results"]:
            try:
                content = scrape_website(url)
                body_content = extract_body_content(content)
                cleaned_content = cleaned_body_content(body_content)
                st.session_state["dom_content"] += cleaned_content + "\n\n"

            except Exception as e:
                st.error(f"Error scraping {url}: {e}")

if st.session_state["dom_content"]:
    st.subheader("Scraped Content")
    parse_description = st.text_area("Extracted Content", st.session_state["dom_content"], height=300)

    st.text_area("Parse the content, you can ask anything")
    if st.button ("Parse Content"):
        dom_chunks = split_dom_content(st.session_state.dom_content)
        parsed_result = asyncio.run(parse_with_ai(dom_chunks, parse_description))
        st.write(parsed_result)

