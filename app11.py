import streamlit as st
import pandas as pd
import os
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px     # 이걸 불러와야 차트를 그릴 수 있다.


def main():
    # 스트림릿에서 제공해주는 차트
    # line_chart, area_chart

    df1 = pd.read_csv('data2/lang_data.csv')

    st.dataframe(df1)

    lang_list = df1.columns[1:]
    choice_list = st.multiselect('언어를 선택해주세요.', lang_list)

    if len(choice_list) != 0 :
        df_choice = df1[choice_list]

        st.dataframe(df_choice)

        # 스트림릿이 제공하는 line_chart
        st.line_chart(df_choice)
        # 스트림릿이 제공하는 area_chart
        st.area_chart(df_choice)

    df2 = pd.read_csv('data2/iris.csv')

    # 스트림릿이 제공하는 bar_chart
    st.bar_chart(df2.iloc[ : , 0: -2 + 1 ])  #문자열 컬럼이 있으면 오류가 나서 문자열 컬럼만 제외함.

    # web 에서 사용할 수 있는 차트 라이브러리 중 
    # Altair 차트 (streamlit 설치 시 같이 설치됨.)
    
    
    alt_chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species'
        )
    st.altair_chart(alt_chart)

    # 스트림릿의 map 차트
    df3 = pd.read_csv('data2/location.csv', index_col = 0)
    st.dataframe(df3)

    st.map(df3)

    # plotly 라이브러리를 이용한 차트 그리기

    df4 = pd.read_csv('data2/prog_languages_data.csv')

    st.dataframe(df4)

    # plotly의 pie 차트 
    fig1 = px.pie(df4, names='lang', values='Sum', title = '각 언어별 파이차트')

    st.plotly_chart(fig1)

    # plotly의 bar 차트
    
    df4_sorted = df4.sort_values('Sum', ascending= False)

    fig2 = px.bar(df4_sorted, x= 'lang', y = 'Sum')

    st.plotly_chart(fig2)




   




if __name__ == '__main__':
    main()