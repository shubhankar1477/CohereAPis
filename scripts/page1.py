import streamlit as st
from utils.CommonUtils import ClsCommonUtils
from scripts.apiCall import ClsApiRun

class ClsUserInterface:
    def __init__(self):
        print("Instance of WebApp created")
        self.api = ClsApiRun()

    def summarize(self):
        sentence = st.text_area('Please paste your article :', height=30)
        button = st.button("Summarize")
        with st.spinner("Generating Summary.."):
            if button and sentence:
                summary = self.api.callApi(sentence)
                st.write(summary)




