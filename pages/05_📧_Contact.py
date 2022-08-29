#Importing the necessary libraries. Lines 2-4.
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#Function used for calling the LOTTIE files. Lines 8-13.
@st.cache(allow_output_mutation=True)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()


#Page configuration settings. Lines 17-20.
st.set_page_config(
    page_title = 'Contact',
    page_icon = '🌅'
)


#Code to display the "MAIL" animation in the sidebar. Lines 23-27.
with st.sidebar:
   url1 = "https://assets7.lottiefiles.com/packages/lf20_in4cufsz.json" 
   res1_json = load_lottieurl(url1)
   st_lottie(res1_json)


#Code to display the HEADER and the small message about the page. Lines 31-32.
st.header(":mailbox: Get In Touch With Me!")
st.write("If you have any suggestions or facing any issues with this web application, then do fill out the following form!")



contact_form = """
<form action="https://formsubmit.co/7587106c738ad7f17c67dd78b6ed2aca" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""



st.markdown(contact_form, unsafe_allow_html=True)

#To use the Local CSS File. Lines 51-55.
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")        


        
url2 = "https://assets7.lottiefiles.com/packages/lf20_g4nzoqba.json" 
res2_json = load_lottieurl(url2)
st_lottie(res2_json)
