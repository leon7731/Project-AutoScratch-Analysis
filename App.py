import streamlit as st

import OTSU_Threshold_Functions as OTTF

### APP Configurations ###
st.set_page_config(page_title="Project AutoScratch Analysis", 
                   page_icon=r"Assets\Fav\favicon.ico", 
                   layout="centered", 
                   initial_sidebar_state="auto", 
                   menu_items=None)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title("Project AutoScratch Analysis") # Title of the App

### Project Introduction & Objective ###
with st.expander("Project AutoScratch Analysis Objective"):
     st.write("""
        Project AutoScratch Analysis is a tool that is used for Automating the process of 
        analyzing and quantifying cell migration parameters such as speed, persistence, and polarity.
         
        -   Objective:
            - To analyze the cell migration parameters of a given image.
            - To quantify the cell migration parameters of a given image with Custom Healing Rate for each Patient.
            - Automate the process of analyzing and quantifying cell migration parameters with various AI algorithm.
         """)
     st.image("Assets\multiple_scratch.jpg")
     
### AutoScratch Algorithm Selection ###     
with st.expander("AutoScratch Algorithm Selection"):
    # Create Radio Buttons
    Algorithm_Selection=st.radio(label = 'The following algorithms are available for AutoScratch Analysis:', 
             options = ['OTSU Threshold','CNN','ANN'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    
    if Algorithm_Selection == 'OTSU Threshold':
        OTTF.OTSU_Analysis_Main()
    elif Algorithm_Selection == 'CNN':
        st.image(r"Assets\Error 404\404 Error.png") 
    elif Algorithm_Selection == 'ANN':
        st.image(r"Assets\Error 404\404 Error.png")
        