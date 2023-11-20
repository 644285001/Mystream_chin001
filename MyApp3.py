import streamlit as st

st.title('การทำนายการลาออกของพนักงาน')
st.header('นาย ชินวัฒน์ ภูไชยแสง')
st.subheader('สาขาวิชาวิทยาการข้อมูล')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/Resignation.png')
with col2:
    st.image('./pic/Resignation2.png')

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ข้อมูลของพนักงาน</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd

raw_data=pd.read_csv('./data/Employee3.csv')
st.write(raw_data.head(10))

html_2 = """
<div style="background-color:#FFBF00;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายคลาสการลาออกของพนักงาน</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")   

s1 = st.number_input("กรุณาเลือกข้อมูล Education", step=1, format="%d")
s2 = st.slider("กรุณาเลือกข้อมูล JoiningYear",2012,2018)
s3 = st.number_input("กรุณาเลือกข้อมูล City", step=1, format="%d")
s4 = st.number_input("กรุณาเลือกข้อมูล PaymentTier", step=1, format="%d")
s5 = st.number_input("กรุณาเลือกข้อมูล Age", step=1, format="%d")
s6 = st.number_input("กรุณาเลือกข้อมูล Gender", step=1, format="%d")
s7 = st.number_input("กรุณาเลือกข้อมูล EverBenched", step=1, format="%d")
s8 = st.number_input("กรุณาเลือกข้อมูล ExperienceInCurrentDomain", step=1, format="%d")


from sklearn.ensemble import RandomForestClassifier
import numpy as np

if st.button("ทำนายผล"):
