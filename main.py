# This is a sample Python script.
from scripts.page1 import ClsUserInterface
import streamlit as st
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    objUi = ClsUserInterface()# Press ⌘F8 to toggle the breakpoint.
    objUi.summarize()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.title("Summarizer using Cohere Api")
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
