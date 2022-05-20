from sqlalchemy import column
import streamlit as st
import pandas as pd

def run_eda():
    st.subheader('EDA 화면')

    df = pd.read_csv('data2/iris.csv')

    # 컬럼이름을 보여주시고
    # 여러 컬럼들 선택 가능 토록 하여, 
    # 선택한 컬럼들만 화면에 보여줍니다.
    # 상관계수를 구하여 화면에 보여줍니다. 

    column_list = st.multiselect('컬럼 선택', df.columns)

    if len(column_list) != 0 :          # empty 안 보이게 만들기
        st.dataframe(df[column_list])

    # 상관계수를 구하여 화면에 보여줍니다.
    if len(column_list) != 0 :
        st.dataframe(df[column_list].corr())
