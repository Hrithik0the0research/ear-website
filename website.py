import streamlit as st
import cv2
import numpy as np
import  matplotlib.pyplot as plt
import random
from glob import glob
from keras.models import load_model
import skimage.io as sk
st.set_page_config(page_title='EAR-BIOMETRICS-HOME', layout = 'wide', page_icon = 'logo.png', initial_sidebar_state = 'auto')
def find_contours(mask):
    cont,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    c=max(cont,key=cv2.contourArea)
    c1=c.reshape(c.shape[0],1*2)
    return c1
st.image("logo.png",width=200)
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
demo=glob("./web-dataset/*")
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
model_names=[" ","Autoencoder","GNN","DNN-E"]
model = st.selectbox("select model",model_names)
if model!=" ":
    if model=="Autoencoder":
        model=load_model("autoencoder.h5")
    elif model=="GNN":
        model=load_model("gnn.h5")
    else:
        model=load_model("dnn.h5")

demo_file = st.selectbox("Download demo images",demo)
with open(demo_file, "rb") as file:
        btn = st.download_button(
                label="Download demo images",
                data=file,
                file_name="demo.png")

uploaded_file = st.file_uploader("Upload an image")
if uploaded_file:
    file_name="fig"+"hrithik"+str(random.randrange(1,100))+".png"
    with open(file_name, mode='bx') as f:
        f.write(uploaded_file.getvalue())
    image=sk.imread(file_name)
    can=[]
    #for i in image:
    img_blur = cv2.GaussianBlur(image,(3,3),sigmaX=0, sigmaY=0) 
#print(img_blur)
    edges = cv2.Canny(image=img_blur, threshold1=150, threshold2=255) 
    #can.append(edges)
    c1=find_contours(edges)
    max_contour =c1
    ellipse = cv2.fitEllipse(max_contour)
#cv2.ellipse(img_array[0][0], ellipse, (255, 255, 255), 2)
    center = tuple(map(int, ellipse[0]))
    val2=[]
    cv2.line(image,center,c1[20],(255,255,255),1)
    cv2.line(image,center,c1[40],(255,255,255),1)
    cv2.line(image,center,c1[60],(255,255,255),1)
    cv2.line(image,center,c1[80],(255,255,255),1)
    cv2.line(image,center,c1[100],(255,255,255),1)
    cv2.line(image,center,c1[120],(255,255,255),1)
    cv2.line(image,center,c1[140],(255,255,255),1)
    cv2.line(image,center,c1[160],(255,255,255),1)
    cv2.line(image,center,c1[180],(255,255,255),1)
    plt.axis("off")
    
    plt.imshow(image)
    plt.savefig("compare.jpg")

    g=0
    if len(c1)>99:
        dg=c1

        dg1=len(c1)//100
        for i in range(0,len(dg),dg1):
            g+=1
            s=(((center[0]-c1[i][0])**2)+((center[1]-c1[i][1])**2))**(1/2)
            val2.append(s)
    val2=np.array(val2[:100])
    #val2=val2[:100]
    val2=val2.reshape(1,val2.shape[0])
    pred=model.predict(val2)
    name=np.argmax(pred)
    st.write("scanning image is :")
    st.image("compare.jpg")
    name_list=["Hitesh","Labhesh","Tarun","Varkha"]
    st.write("This is the ear of :",name_list[name])
          
