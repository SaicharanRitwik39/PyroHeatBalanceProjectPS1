#Importing the necessary libraries. Lines 2-6.
import time
import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie


#Function used for calling the Lottie files. Lines 10-15.
@st.cache(allow_output_mutation=True)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()
    

#Page configuration settings. Lines 19-22.
st.set_page_config(
    page_title = 'Guidelines',
    page_icon = '📖'
)



#Columns to define the "HEADER" of the page. Lines 27-37.
col1, col2 = st.columns([1,2])
with col1:
    url1 = "https://assets10.lottiefiles.com/packages/lf20_p7ml1rhe.json" #Code to display the NOTES GIF from Lottie Library.
    res1_json = load_lottieurl(url1)
    st_lottie(res1_json)
with col2:
    st.markdown(""" <style> .font {
                font-size:35px ; font-family: 'Cooper Black'; color: #1BA6C4;} 
                </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">NOTES</p>', unsafe_allow_html=True) 
    st.write("Let's walk you through the web application.")
    
    
    

#Code for the "CLICK ME" and the "THE DASHBOARD" sections. Lines 43-71.     
col1, col2 = st.columns(2)
with col1:
    with st.expander("CLICK ME"):
         url2 = "https://assets5.lottiefiles.com/packages/lf20_lcmpz7.json" #Code to display the NOTES GIF from Lottie Library.
         res2_json = load_lottieurl(url2)
         st_lottie(res2_json)
         st.write("1. You must have gotten familiar with the **NAVIGATION** section in the sidebar to your left. These are the various pages of the web application.")
         st.write("a) **Intro:** This is the page that you saw as soon as you opened the web application.") 
         st.write("b) **User Notes:** The page you are on right now!")   
         st.write("c) **Dashboard:** This is the **focal page** of the web app. All the **calculations** and **metrics** will be displayed on this page.") 
         st.write("d) **Demo:** In case you have any queries about the functionalities of this app, I have created a YouTube video to help you out.")
         st.write("e) **Contact:** I have added a form on this page for taking further suggestions and inputs from you... :smiley:!")
         st.write("***")   
         
            

with col2:
    with st.expander("THE DASHBOARD !!!"):
         url3 = "https://assets2.lottiefiles.com/packages/lf20_acryqbdv.json" #Code to display the Dashboard GIF from Lottie Library.
         res3_json = load_lottieurl(url3)
         st_lottie(res3_json)
         
         st.write("This page is primarily divided into 3 sections:")
         st.write("i) **Metrics:** This section displays all the important parameters involved in establishing the Heat Balance in cement plants. These include the **Datum Pressure**, **Clinker Capacity(tph and tpd)**, **Ambient Temperature**, **Cooler Efficiency** and **Cooler Heat Losses**.")
         st.write("ii) **Inputs:** In this section, you have to enter the following information: **Temperatures**, **Static Pressures**, **Diameters**, **Fan Outlet Pressures**, **Power**, **Pitot Tube Constants** and some **General Information**. It is divided into 7 tabs. Choose the respective tabs to fill up the information.")
         st.write("iii) **Results:** You can click on the respective option under the **Results** menu to view and download the results.")   
            
            
         st.warning('Currently session state variables across the pages are not supported. Once you begin working with the dashboard do not open any other page, otherwise your progress will be lost!')   
         



#Code for the "EXCEL UPLOADS" section. Lines 77-130. 
with st.expander("EXCEL UPLOADS"):
     st.write("***")
     col1, col2, col3 = st.columns([1,3,1])

     with col1:
          st.write("")

     with col2:
          image = Image.open('Excels.png')
          st.image(image)         

     with col3:
          st.write("")  
            
     st.write("***")
    
     st.markdown(""" <style> .font {
                font-size:20px ; font-family: 'Cooper Black'; color: #1BA6C4;} 
                </style> """, unsafe_allow_html=True)
     st.markdown('<p class="font">Dynamic Pressures and Velocities Excel Sheet</p>', unsafe_allow_html=True) 
     
     st.write("""Make sure that the data for these quantities is in the order as given below (columnwise):

**Dynamic Pressure** Values of:
* Preheater Downcomer Ducts
* Tertiary Air Ducts
* Cooler Mid Air Ducts
* Cooler Vent Air Ducts
* ESP Stack Duct
then the **Velocities** of:
* Cooler Fans 
and finally the **Dynamic Pressure** Values of,
* Kiln Blowers
* Calciner Blowers
* PA Fans
     """)
     st.write("If you have any doubt, you may click on the **'EXCEL FILE EXAMPLE'** link to see how your input excel should look like.")
     st.markdown("[EXCEL FILE EXAMPLE](https://drive.google.com/file/d/1CNGLBLcFnylBkYjmMGMORRFZBh01sH5i/view?usp=sharing)")  #Pic showing a sample "INPUT EXCEL SHEET".
     st.write("***")
        
     st.markdown(""" <style> .font {
                font-size:20px ; font-family: 'Cooper Black'; color: #1BA6C4;} 
                </style> """, unsafe_allow_html=True)
     st.markdown('<p class="font">Kiln Surface Temperatures Excel Sheet</p>', unsafe_allow_html=True) 
     
    
     st.write("""
Whereas, for this excel file that you are going to upload, keep in mind the following details:
* The first meter starts from the kiln outlet side.
* "Interval" is the distance between consecutive temperature readings. For example, when surface temperature was measured every 3 meters, the interval would be 3.
* Multiple temperature readings can be provided at each point by putting them in separate excel columns. In such a case, the **average** of the readings will be automatically computed.
* Fill the columns in the Input Excel starting from column A and use columns B,C,D,... as required. Columns should contain only the temperature readings in numbers and nothing else, not even column headers!
""")
     st.write("***")
    
    

# Code for the "TEMPLATE EXCEL FEATURE". Lines 135-140.    
with st.expander("TEMPLATE EXCEL FEATURE"):
     st.write("***")
     image = Image.open('Template.png')
     st.image(image) 
     st.write("***")   
     st.write("If you want, then after filling up the information in the **'GENERAL INFORMATION ABOUT YOUR DATA'** tab, an file excel will be automatically generated. You can store the Dynamic Pressure and Velocity values in this excel sheet and upload it for further computations.")
        
        

        
#Code for the "METRICS" expander. Lines 146-178.        
with st.expander("METRICS"):
    st.write("***")
    image = Image.open('Metrics.png')
    st.image(image)
    st.write("This is the final section of the dashboard. The above quantities are calculated as follows:")
    col1, col2 = st.columns([2,1])
    with col1:
         st.write("i) **Datum Pressure:** The mean sea level has to be entered by the user. Depending on the msl, the datum pressure can be calculated using the formula:")
         st.latex("10336*pow(e,-0.0001255*msl)")
         st.write("ii) **Clinker Capacity (tph):** The clinker capacity is calculated using the formula:")
         st.latex(" (KilnFeed)/(KilnFeedFactor)")   
         st.write("This is converted to tpd by multiplying by 24.")
           
    with col2:
        url4 = "https://assets6.lottiefiles.com/packages/lf20_Pq51ZX.json" 
        res4_json = load_lottieurl(url4)
        st_lottie(res4_json)
        
        
    col1, col2 = st.columns([1,2])
    with col1:
         url4 = "https://assets6.lottiefiles.com/packages/lf20_buzt1erl.json" 
         res4_json = load_lottieurl(url4)
         st_lottie(res4_json) 
         
    with col2:
         st.write("iii) **Ambient Temperature:** The ambient temperature is an input by the user. By default the software takes the value of 30 celsius.") 
         st.write("iv) **Cooler Efficiency(%):** Whenever the impact of **thermal recuperation capacity** of pyro process in cement plants is to be evaluated, that of the **cooler** is usually of utmost importance. This is calculated using the formula:")
         
         
    st.latex("Efficiency = (Heat Input-Heat Losses)/Heat Input")  
 
    st.write("***")     
    
    

#Code explaining the "COOLER VENT AIR BACK CALCULATION" procedure. Lines 183-215.    
with st.expander("COOLER VENT AIR BACK CALCULATION FEATURE"):
     st.write("***")
     st.write("In case the user wants to **back calculate** the Cooler Vent Air flow, then the following expander will pop up under the Fan Flows section:")
     image = Image.open('CVAbackcalc.png')
     st.image(image)
        
     st.write("Back calculation is performed by taking the ESP Stack flow into account. Let us say (for the sakeof an example), the ESP flow (in Nm 3/kgcl) is 0.71. This is converted into kg/kgcl by multiplying it with the cooler air density, an input taken in the ‘General Information about your Data’ expander (Q.11 in section 3.1). Also, suppose that the cooler air density is 1.285. Using mass and heat conservation principles, one has to solve a system of two linear equations in two variables. The two variables are X and Y . X is the Cooler Vent Air Flow and Y is the False Air Flow, both in kg/kgcl. Using mass balance, one gets the following equation:")
     st.latex("X + Y = (ESP Stack Flow) ⋅ (Cooler Air Density).")
     st.write("In this case the exact equation becomes:")
     st.latex("X + Y = (0.71) ⋅ (1.285)")
     st.latex("\Rightarrow X+Y = 0.908327    (a)")   
     st.write("The other equation is obtained via heat balance. Say the temperature of the Cooler Vent Air is 338°C , the temperature of ESP Stack is 296°C and the ambient temperature is 35°C . The formula for the heat content is m ⋅ Cp ⋅ ΔT. The ΔT is calculated by subtracting the reference temperature.")
     st.write("The formula for Cp is:")   
     st.latex("0.237 + (23*T*10 ^ -6)")
     st.write("So, the heat contained in the Cooler Vent Air flow is:") 
     st.latex("(338 − 20) ⋅ (0.237 + (23 ⋅ 338 ⋅ 10−6)) ⋅X.") 
     st.write("The heat contained in the False Air Flow is:")   
     st.latex("(35 − 20) ⋅ (0.237 + (23 ⋅ 30 ⋅ 10−6)) ⋅ Y.")
     st.write("And, finally the heat contained in the Flow taken at Stack (K) is:")
     st.latex("(296 − 20) ⋅ (0.237 + (23 ⋅ 296 ⋅ 10−6)) ⋅ (0.909327).")
     st.write("Upon simplification and balancing the heat, we get the following equation:")
     st.latex("82.73361 ⋅ X + 8.323175 ⋅ Y = 65.55141     (b)")
     st.write("Solving equations (a) and (b), we get:")
     st.latex("X = 0.779343, Y = 0.128984")
     st.write("The code for this has been implemented using the SciPy library in Python. It employs the traditional method of using basic linear algebra (matrices and vectors) to arrive at the final solution.")  
    
     st.write("***")
    
     image = Image.open('CVAschematic.png')
     st.image(image)
     st.caption("Cooler Vent Air Back Calculation Schematic.")
    
     st.write("***")
        
    

#Code for the rest of the stuff on the main page. Lines 220-246. Python libraries etc. 
st.write("***")    

st.write("The reference temperature (NTP) considered for the calculations is **20 degree celsius**.")
st.write("That's it! You are all set to use this app now. Now go ahead and start working with the dashboard!!!")

st.write("***")
    
libraries = st.selectbox(
             'Would you like to see the Python Libraries used to make this app?',
              ('No', 'Yes'))
if (libraries == 'Yes'):
      st.write("1. streamlit")
      st.write("2. base64")
      st.write("3. json")
      st.write("4. requests")
      st.write("5. numpy")  
      st.write("6. array")
      st.write("7. pandas") 
      st.write("8. math")
      st.write("9. scipy")  
      st.write("10. streamlit-aggrid")
      st.write("11. streamlit-lottie")
      st.write("12. annotated-text")
      st.write("13. streamlit-option-menu") 
      st.write("14. matplotlib") 
      st.write("15. time")  
      st.write("16. PIL(Python Imaging Library)")  
    
    
#Code to display the "LAPTOP" animation in the sidebar from LOTTIE. Lines 250-253.
with st.sidebar:
    url1 = "https://assets5.lottiefiles.com/packages/lf20_obzwm19d.json" #Code to display the NOTES GIF from Lottie Library.
    res1_json = load_lottieurl(url1)
    st_lottie(res1_json)          


#Code to display the "BLUE LINE" animation from Lottie. Lines 257-259.
url3 = "https://assets2.lottiefiles.com/packages/lf20_4m0f2coq.json"  #"BLUE LINE" animation from Lottie. To separate the 2 sections.
res3_json = load_lottieurl(url3)
st_lottie(res3_json)
