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

splen = st.number_input("กรุณาเลือกข้อมูล Education", step=1, format="%d")
splen = st.number_input("กรุณาเลือกข้อมูล JoiningYear", step=1, format="%d")
splen = st.number_input("กรุณาเลือกข้อมูล City", step=1, format="%d")
splen = st.number_input("กรุณาเลือกข้อมูล PaymentTier", step=1, format="%d")
splen = st.number_input("กรุณาเลือกข้อมูล Age", step=1, format="%d")
splen = st.number_input("กรุณาเลือกข้อมูล Gender", step=1, format="%d")
splen = st.number_input("กรุณาเลือกข้อมูล EverBenched", step=1, format="%d")
splen = st.number_input("กรุณาเลือกข้อมูล ExperienceInCurrentDomain", step=1, format="%d")

from sklearn.model_selection import train_test_split
import numpy as np

if st.button("ทำนายผล"):
    X= raw_data.drop(columns='LeaveOrNot')
    y=raw_data['LeaveOrNot']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=20, test_size=0.3)

    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)

    #ข้อมูล input สำหรับทดลองจำแนกข้อมูล
   x_input = np.array([[Education,JoiningYear,City,PaymentTier,Age,Gender,EverBenched,ExperienceInCurrentDomain]])
    # เอา input ไปทดสอบ
   st.write(rf.predict(X_test))
   out=rf.predict(X_test)

    if out[0]==0:
      #st.image("./pic/iris.jpg")
      st.header("อยู่ต่อ")
    else:
      #st.image("./pic/iris1.jpg")  
      st.header("มีแนวโน้มว่าจะลาออก")
    st.button("ไม่ทำนายผล")
else :
    st.button("ไม่ทำนายผล")