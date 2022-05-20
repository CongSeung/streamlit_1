import streamlit as st
import pandas as pd
import os
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns





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




if __name__ == '__main__':
    main()