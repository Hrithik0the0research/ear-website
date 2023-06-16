import streamlit as st
st.set_page_config(page_title='EAR-BIOMETRICS-ABOUT', layout = 'wide', page_icon = 'logo.png', initial_sidebar_state = 'auto')
st.title("Motivation")
wr="""
The goal of this research study is to emphasize the rising interest in ear recognition as a biometric technique, as well as the potential advantages it has over other non-contact biometrics such as facial recognition. The study report also underlines the need for more research and development in this field, notably in resolving lighting, occlusion, and uniqueness concerns.
The review of existing literature gives a thorough overview of the present state-of-the-art in-ear detection and recognition, which might be valuable for researchers and practitioners interested in pursuing this method. The study also emphasizes the availability of ear databases for academics to utilize in building and testing ear identification systems.
"""
st.write(wr)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .main {background-color: #f8f9d2;
     background-color: #b8c6db;
background-image: linear-gradient(315deg, #b8c6db 0%, #f5f7fa 74%);
color:black;
            
            
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)