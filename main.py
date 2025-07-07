import streamlit as st
from Scrape import (scrape_website,split_dom_content,clean_body_content,extract_body_content,)

from parse import parse_with_ollama



#adding a title for our website
st.title("AI WEB SCRAPER")
#url input box
url= st.text_input("Enter a website url:  ")

if st.button("Scrape Site"):
    st.write("scrapping the website")
    result =scrape_website(url)
    #print(result)
    body_content=extract_body_content(result)
    cleaned_content=clean_body_content(body_content)
# making a session
    st.session_state.dom_content= cleaned_content

    with st.expander("view dom content"):
        st.text_area("dom content",cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description=st.text_area("describe what u wanna parse?")

    if st.button("Parse content"):
        if parse_description:
            st.write("parsing the content")

            dom_chunks=split_dom_content(st.session_state.dom_content)
            result= parse_with_ollama(dom_chunks,parse_description)
            st.write(result)
