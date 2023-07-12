#import modules
import streamlit as st
import pickle
import pandas as pd
import math
import numpy as np


#import the model
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")

#form
company=st.selectbox("Brand",df["Company"].unique())
type=st.selectbox("Type",df["TypeName"].unique())
ram=st.selectbox("Ram(in GB)",[2,4,6,8,12,16,24,32,64])
weight=st.number_input('Weight')
touchscreen=st.selectbox("Touchscreen",["NO","YES"])
ips=st.selectbox("IPS Display",["NO","YES"])
screen_size=st.number_input('Screen Size')
resolution=st.selectbox("Screen Resolution",['1024x576', '1152x648', "1280x720", "1366x768", "1600x900", "1920x1080", "2560x1440", "3840x2160", "7680x4320"])
cpu=st.selectbox("CPU",df["Cpu brand"].unique())
hdd=st.selectbox("HDD(in GB)",[0,128,256,512,1024,2048])
ssd=st.selectbox("SSD(in GB)",[0,8,128,256,512,1024])
gpu=st.selectbox("GPU",df["Gpu brand"].unique())
os=st.selectbox("OS Type",df["os"].unique())

#button
if  st.button('Predict Price'):
    pass

#taking input into model
if touchscreen=='Yes':
    touchscreen=1
else:
    touchscreen=0

if ips=='Yes':
    ips=1
else:
    ips=0


X_Res=int(resolution.split('x')[0])
Y_Res=int(resolution.split('x')[1])

try:
   ppi=((X_Res**2)+(Y_Res**2))**0.5/screen_size

except ZeroDivisionError:
    ppi=0


print(ppi)  # 👉️ 0


query=np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
query=query.reshape(1,12)
st.title("The Predicted Price of this configuration is " + str(np.exp(pipe.predict(query)[0])))