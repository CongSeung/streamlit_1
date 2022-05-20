# 파일 여러개 올리는 방법

import imp
import streamlit as st
import pandas as pd
import os
from PIL import Image
from datetime import datetime

###########################################################################
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
###########################################################################

# streamlit area

def main() :
    st.title('여러 파일 한번에 업로드하는 앱')

    # 사이드 바용 메뉴
    menu = ['Image', 'CSV' , 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    # accept_multiple_files 을 True 로 세팅하면
    # 여러 파일들을 한번에 받을 수 있다.
    if choice == menu[0] :
        upload_files = st.file_uploader('이미지 파일 업로드',
                       type = ['jpg', 'png' , 'jpeg'], 
                       accept_multiple_files= True)
        # upload_files 는 여러 파일들을 담고 있는 리스트이다.
        # 업로드 파일이 있는 경우에만, 아래 코드를 실행해야 한다.
        
        if upload_files is not None :
            # for 문을 사용한 이유는 upload_files 가 여러 데이터가 있는 리스트이기 때문에
            # 하나씩 가져와 temp 폴더에 저장할 것이다.
            for file in upload_files :
                current_time = datetime.now()
            
                new_filename = current_time.isoformat().replace(':', '_') + '.png'

                file.name = new_filename

                save_uploaded_file('temp', file)

            # 저장된 파일 화면에 띄워지게 만들기
            for file in upload_files:
                img = Image.open(file)
                st.image(img)
        
    # CSV 파일을 여러 개 올리면 이 파일들을 temp 에 저장하고
    # 데이터프레임으로 읽어서 화면에 표시!
    elif choice == menu[1] :
        upload_files = st.file_uploader('이미지 파일 업로드',
                       type = ['csv'], 
                       accept_multiple_files= True)
        # upload_files 는 여러 파일들을 담고 있는 리스트이다.
        # 업로드 파일이 있는 경우에만, 아래 코드를 실행해야 한다.
        
        if upload_files is not None :
            # for 문을 사용한 이유는 upload_files 가 여러 데이터가 있는 리스트이기 때문에
            # 하나씩 가져와 temp 폴더에 저장할 것이다.
            for file in upload_files :
                current_time = datetime.now()
            
                new_filename = current_time.isoformat().replace(':', '_') + '.csv'

                file.name = new_filename

                save_uploaded_file('temp', file)

            # 저장된 파일 화면에 띄워지게 만들기
            for file in upload_files:
                df = pd.read_csv(file)
                st.dataframe(df)



if __name__ == '__main__' :
    main()