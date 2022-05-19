from os import stat
from scipy.misc import ascent
from sqlalchemy import asc
import streamlit as st
import pandas as pd


def main():
    df = pd.read_csv('data2/iris.csv')

    # 버튼 만들기 - 버튼을 누르면 데이터가 보이게
    if st.button('데이터보기') :            # button 자체가 0과 1로 값이 나오게 됨.
        st.dataframe(df)                   # 버튼을 누를 때마다 새로 시작됨.

    # '대문자' 버튼을 만들고 버튼을 누르면 
    # species 컬럼의 값들을 대문자로 변경한
    # 데이터 프레임을 보여주세요.
    
    if st.button('대문자') :
        df['species'] = df['species'].str.upper()
        st.dataframe(df)

### 한 번에 여러 줄 주석하기. 드래그로 긁고 컨트롤 슬래쉬
    #  if st.button('대문자') :
    #     st.dataframe(df['species'].str.upper())     
    # 
    # 라디오 버튼 : 여러 개중에 한 개 선택할 때
    my_order = ['오름차순 정렬', '내림차순 정렬']      

    status = st.radio('정렬방법 선택', my_order)  # 라디오 버튼은 1과 0이 아닌 들어가 있는 값을 띄게 된다.

    if status == my_order[0] :
        #petal_length 컬럼을 오름차순으로 정렬하여 보여준다.
        # df.sort_values('petal_length')
        st.dataframe(df.sort_values('petal_length'))
    elif status == my_order[1] :
        #petal_length 컬럼을 내림차순으로 정렬하여 보여준다.
        # df.sort_values('petal_length', ascending= False)
        st.dataframe(df.sort_values('petal_length', ascending=False))

    status = st.radio('정렬방법 선택2', my_order)  # 라디오 버튼은 1과 0이 아닌 들어가 있는 값을 띄게 된다.

    if status == my_order[0] :
        #petal_length 컬럼을 오름차순으로 정렬하여 보여준다.
        df = df.sort_values('petal_length')
        st.dataframe(df)
    elif status == my_order[1] :
        #petal_length 컬럼을 내림차순으로 정렬하여 보여준다.
        df = df.sort_values('petal_length', ascending= False)
        st.dataframe(df)

    # 체크박스 : 체크 해제 / 체크
    if st.checkbox('헤드 5개 보기') : 
        st.dataframe(df.head())
    else :
        st.text('누르면 헤드 나옴')

    # 셀렉트 박스 : 여러 개중에 한 개만 고르는 것
    language = ['Ptyhon','C','Java','Go','PHP']

    my_choice = st.selectbox('좋아하는 언어 선택', language)

    if my_choice == language[0]:
        st.write('파이썬을 좋아하는구나.')
    elif my_choice == language[1]:
        st.write('C 언어를 좋아하는구나.')
    elif my_choice == language[2]:
        st.write('Java를 좋아하는구나.')
    elif my_choice == language[3]:
        st.write('GO를 좋아하는구나.')
    else :
        st.write('PHP를 좋아하는구나.')

    # 멀티셀렉트 박스 : 여러 개를 고를 수 있는 박스

    my_choice = st.multiselect('여러 개 선택 가능', language)
    
    # 멀티셀렉트를 이용해서, 특정 컬럼들만 가져오기
    # 유저에게, iris df 의 컬럼들을 다 보여주고,
    # 유저가 선택한 컬럼들만, 데이터프레임을 화면 보여줄것.

    columns_list = df.columns

    choice_list = st.multiselect('컬럼을 선택하세요', columns_list)

    st.dataframe(df[choice_list])

    # 슬라이더 : 숫자를 조정할 때 유용한 기능
    # 소수점을 나오게 하려면 모든 값을 소수점으로 만들어주어야 함
    # st.slider('나이', 1.0 , 120.0 , 30.0 , 0.1)
    age = st.slider('나이', 0, 120, 20, 1)

    st.text('제 나이는 {} 살 입니다.'.format(age))
    
    # 익스펜더 (확장할 수 있는 영역)
    with st.expander('hello'):
        st.text('안녕하세요.')
        st.dataframe(df)
    

if __name__ == '__main__' :
    main()