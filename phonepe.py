import pandas as pd
import json
import os
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#streamlit page creation
st.set_page_config(page_title= "Phonepe Pulse Data Visualization ",                 
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   )
st.title(":violet[:iphone:**Phonepe Pulse Data Visualization**:bar_chart:]")
st.sidebar.title(":red[Overview of the Project]")
#option menu
option = option_menu(menu_title=None,
                     options=['Phonepe Map','Analysis','Visualization'],
                     icons=['geo-alt', 'file-bar-graph', 'file-bar-graph'],
                     orientation='horizontal',
                     menu_icon="app-indicator",
                     styles={"nav-link": {"font-size": "25px", "text-align": "center", "margin": "-1px",
                                          "--hover-color": ""},
                             "nav-link-selected": {"background-color": "#9370DB"}})
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)
