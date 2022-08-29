#Importing the necessary libraries. Lines 2-4.
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#Function used for calling the Lottie files. Lines 8-13.
@st.cache(allow_output_mutation=True)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()


#PAGE CONFIGURATION settings. Lines 17-20.
st.set_page_config(
    page_title = 'Demo',
    page_icon = '📺'
)


#Code to display the Lottie animation in the sidebar. Lines 24-27.
with st.sidebar:
   url1 = "https://assets8.lottiefiles.com/packages/lf20_ehfMXK.json" 
   res1_json = load_lottieurl(url1)
   st_lottie(res1_json)
 

#Code to display the YouTube Icon via Lottie Library and the video link. lines 31-38.    
col1, col2 = st.columns([2,1])
with col1:
  st.title("DEMO")
  st.write("For a demo of the Web Application, you may refer to the following video:") 
with col2:
  url1 = "https://assets2.lottiefiles.com/private_files/lf30_cwyafad8.json"
  res1_json = load_lottieurl(url1)
  st_lottie(res1_json)


#YouTube video URL. Lines 42-43.
url = 'https://youtu.be/eM6Qcjr2sUs'
st.video(url)
