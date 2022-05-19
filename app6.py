import streamlit as st
import pandas as pd

def main():
    # 유저한테 입력을 받는 방법

    # 1. 이름 입력 받기
    name = st.text_input('이름을 입력하세요.')
    # st.subheader(name + '님 안녕하세요?')

    if name != "":
        st.text(name + '님 안녕하세요?')

    # 2. 입력 글자 갯수 
    address = st.text_input('이름을 입력하세요.', max_chars= 10)
    st.subheader(address)

    

    # 3. 여러 행 입력 가능하도록
    message= st.text_area('입력', height= 5)
    st.subheader(message)

    # 4. 숫자를 입력
    numbers = st.number_input('숫자 입력', 1, 100)

    # 5. 실수를 입력
    numbers = st.number_input('숫자 입력', 1.0, 100.0)

    # 6. 날짜 입력
    my_date = st.date_input('약속 날짜')
    st.write(my_date)

    # 7. 요일 찍기
    st.write(my_date.weekday())
    st.write(my_date.strftime('%A'))

    #8. 시간 입력
    my_time = st.time_input('시간 선택')
    st.write(my_time)

    #9. 색깔 입력
    color = st.color_picker('색을 입력하세요.')
    st.write(color)

    #10. 비밀번호 입력
    password = st.text_input('비밀번호 입력', type = "password")
    




if __name__ == '__main__':
   main()   

