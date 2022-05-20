import imp
from anyio import run_async_from_thread
import streamlit as st
import pandas as pd
import os
from PIL import Image
from datetime import datetime
from app9_About import run_about
from app9_EDA import run_eda
from app9_ML import run_ml
from app9_home import run_home  ###

### 파일을 분리해서 만드는 앱 ###

def main() :
    st.title('파일 분리 앱')

    menu = ['Home', 'EDA', 'ML', 'About']

    choice = st.sidebar.selectbox('메뉴', menu)
    
    # 아래에 처리될 내용을 다른 파이썬 파일에 만든다는 이야기

    if choice == menu[0]:
        run_home()           ### 중요 포인트 같은 디렉토리에 해당 함수를 포함한 파일이 있으면 VSC 는 자동으로 임포트 해준다!
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()
    elif choice == menu[3]:
        run_about()

if __name__ == '__main__' :
    main() 