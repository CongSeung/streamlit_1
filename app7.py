import streamlit as st         # 대시보드 제작 라이브러리
import pandas as pd            # 데이터 확인 가공 라이브러리
from PIL import Image          # 이미지 관련 라이브러리
import os                      # 디렉토리 관련 라이브러리
from datetime import datetime  # 시간 관련 라이브러리
import numpy as np

##### 파일을 업로드하는 방법 #####
##### 이미지 파일, CSV 파일 업로드 #####

# 파일 업로드하는 함수
# 디렉토리 정보와 파일을 알려주면, 해당 디렉토리에
# 파일을 저장하는 함수
def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))



def main ():
    # 사이드 바 만들기
    st.title('파일 업로드 프로젝트')

    menu = ['Image', 'CSV' , 'About']
    choice = st.sidebar.selectbox('MENU', menu)

    if choice == menu[0]:
        st.subheader('이미지 파일 업로드')
        # 기본 골격을 잡아놓고
        upload_file = st.file_uploader('이미지 파일 선택', type = ['jpg', 'jpeg', 'png'])
        if upload_file is not None:
            print(upload_file.name)
            print(upload_file.size)
            print(upload_file.type)

            # 파일명을 유니크하게 만들어서 저장해야 한다.
            # 현재 시간을 활용해서, 파일명을 만든다.
            # 드래그로 탭하면 오른쪽 쉬프트 탭하면 왼쪽
            # 들여쓰기 잘못하면 오류납니다~~~
            current_time = datetime.now()

            print(current_time.isoformat().replace(':', '_'))
            
            new_filename = current_time.isoformat().replace(':', '_') + '.jpg'

            upload_file.name = new_filename
            save_uploaded_file('temp', upload_file)


    elif choice == menu[1]:
        st.subheader('CSV 파일 업로드')
        
        upload_file = st.file_uploader('CSV 파일 선택', type =['csv'])
        if upload_file is not None:

            current_time = datetime.now()

            print(current_time.isoformat().replace(':', '_'))
            
            new_filename = current_time.isoformat().replace(':', '_') + '.csv'

            upload_file.name = new_filename
            save_uploaded_file('temp', upload_file)

    else :
        st.subheader('파일 업로드 프로젝트입니다.')

if __name__ == '__main__':
    main()

