import imp
from pydoc import importfile
import streamlit as st
import pandas as pd

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main():
    # 저장되어있는, 이미지 파일을, 화면에 표시하기
    img = Image.open('data2/image_03.jpg')

    st.image(img)
    st.image(img,use_column_width=True)

    # 인터넷에 있는 이미지 url을 통해 화면에 표시하기

    url = 'https://transcode-v2.app.engoo.com/image/fetch/f_auto,c_limit,w_1280,h_800,dpr_1/https://assets.app.engoo.com/images/1u31QP7nVOZYka3l7iYJmj.jpeg'
    st.image(url)
    st.image(url, use_column_width= True)

    # 저장된 동영상 화면에 표시하기
    video_file = open('data2/secret_of_success.mp4', 'rb')
    st.video(video_file)

    audio_file = open('data2/song.mp3', 'rb')
    st.audio(audio_file.read(), format = 'audio/mp3')

if __name__ == '__main__':
    main()