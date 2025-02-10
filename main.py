import streamlit as st 

st.set_page_config(page_title="Data manager", page_icon="✏️")

st.title("Ai scraper Web")

classique_scrape_page = st.Page("scrapeClassique.py", title= "Scrape your page ", icon="🔍")
multiple_scrape_page = st.Page("scrapeMultiple.py", title= "Scrape multiple pages", icon="💰")

pg = st.navigation([classique_scrape_page, multiple_scrape_page])
pg.run()