#Importing the necessary libraries. Lines 2-5.
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from annotated_text import annotated_text, annotation


#Function used for calling the Lottie files. Lines 9-14.
@st.cache(allow_output_mutation=True)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()


#Page configuration settings. Lines 18-21.
st.set_page_config(
    page_title = 'Hello There!',
    page_icon = ':smiley:'
)


#Code to display the information in the SIDEBAR. Lines 25-45.
with st.sidebar:
    col1, col2 = st.columns( [0.8, 0.5])
    with col1:
      st.markdown(""" <style> .font {
                      font-size:15px ; font-family: 'Cooper Black'; color: #1BA6C4;} 
                      </style> """, unsafe_allow_html=True)
      st.markdown('<p class="font">LETS GET STARTED</p>', unsafe_allow_html=True) 
    with col2:
        url1 = "https://assets5.lottiefiles.com/private_files/lf30_utzio8lv.json"
        res1_json = load_lottieurl(url1)
        st_lottie(res1_json)
    
    annotated_text(
    "Click on the ",
    (" 'USER NOTES' ", "", "#14BF9A"),
    "page above to see how to use this app and what features are available."    
    )  
    
    url2 = "https://assets4.lottiefiles.com/packages/lf20_jnb58ipz.json"
    res2_json = load_lottieurl(url2)
    st_lottie(res2_json)
    
    
    st.write("***")
    

#Code to display the Title and the Lottie animation of the automated machine. Lines 52-65.
col1, col2 = st.columns( [0.8, 0.2])
with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
                        font-size:35px ; font-family: 'Cooper Black'; color: #1BA6C4;} 
                        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">PYRO HEAT BALANCE WEB APPLICATION</p>', unsafe_allow_html=True) 
    
st.markdown("""
Well, Hello there! This software is all you need for establishing the Heat Balance of Pyro systems in Cement Plants. 
""")

url3 = "https://assets6.lottiefiles.com/packages/lf20_04usqfm9.json"
res3_json = load_lottieurl(url3)
st_lottie(res3_json)

st.write("***")
